// Generates tokens.json from atlocal.css, the single source of brand values.
//
//   node scripts/build-tokens.mjs          write tokens.json
//   node scripts/build-tokens.mjs --check  exit 1 if tokens.json is stale
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const css = readFileSync(join(root, "atlocal.css"), "utf8");
const out = join(root, "tokens.json");

const GROUPS = [
  ["gradient-", "gradient"],
  ["font-", "font"],
  ["weight-", "weight"],
  ["text-", "size"],
  ["leading-", "leading"],
  ["tracking-", "tracking"],
  ["space-", "space"],
  ["radius-", "radius"],
  ["shadow-", "shadow"],
];

const tokens = {
  $source: "https://brand.atlocal.ai/atlocal.css",
  $generated: "Do not edit. Run `npm run tokens` after changing atlocal.css.",
  color: {},
};

const decl = /--al-([a-z0-9-]+):\s*([^;]+);(?:[ \t]*\/\*([^*]*)\*\/)?/g;
for (const [, name, rawValue, comment] of css.matchAll(decl)) {
  const value = rawValue.trim();

  if (/^#[0-9a-f]{6}$/i.test(value)) {
    const parts = (comment || "").split("·").map((p) => p.trim()).filter(Boolean);
    const entry = { name: parts[0], hex: value.toUpperCase() };
    const hex = value.slice(1);
    entry.rgb = [0, 2, 4].map((i) => parseInt(hex.slice(i, i + 2), 16));
    for (const p of parts.slice(1)) {
      if (p.startsWith("Pantone ")) entry.pantone = p;
      if (p.startsWith("CMYK ")) entry.cmyk = p.slice(5).split(/\s+/).map(Number);
    }
    if (!entry.name) throw new Error(`--al-${name} needs a "Name · ..." comment`);
    tokens.color[name] = entry;
    continue;
  }

  const group = GROUPS.find(([prefix]) => name.startsWith(prefix));
  if (!group) throw new Error(`--al-${name} has no token group`);
  const [prefix, key] = group;
  (tokens[key] ||= {})[name.slice(prefix.length)] = value;
}

const json = JSON.stringify(tokens, null, 2) + "\n";

if (process.argv.includes("--check")) {
  let current = "";
  try { current = readFileSync(out, "utf8"); } catch {}
  if (current !== json) {
    console.error("tokens.json is out of date with atlocal.css. Run `npm run tokens`.");
    process.exit(1);
  }
  console.log("tokens.json matches atlocal.css");
} else {
  writeFileSync(out, json);
  console.log(`wrote tokens.json (${Object.keys(tokens.color).length} colors)`);
}
