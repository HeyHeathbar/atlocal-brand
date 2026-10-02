// Fails if START_HERE.md links a file that doesn't exist, or if any logo,
// symbol, icon or studio SVG is missing its PNG (or the reverse).
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const problems = [];

const startHere = readFileSync(join(root, "START_HERE.md"), "utf8");
for (const [, path] of startHere.matchAll(/https:\/\/brand\.atlocal\.ai\/([\w./-]+)/g)) {
  if (path && !existsSync(join(root, path))) problems.push(`START_HERE.md links missing file: ${path}`);
}

for (const dir of ["logo", "symbol", "icon", "studio"]) {
  const files = readdirSync(join(root, dir));
  for (const f of files) {
    const [base, ext] = [f.replace(/\.(svg|png)$/, ""), f.split(".").pop()];
    const twin = ext === "svg" ? `${base}.png` : `${base}.svg`;
    if (!files.includes(twin)) problems.push(`${dir}/${f} has no ${twin}`);
    if (!startHere.includes(`${dir}/${base}.`)) problems.push(`${dir}/${f} is not listed in START_HERE.md`);
  }
}

if (problems.length) {
  console.error(problems.join("\n"));
  process.exit(1);
}
console.log("assets match START_HERE.md");
