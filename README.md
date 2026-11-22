# Get To Work mod index

The list of community mods shown in **GTW Mod Manager** under *Browse community mods*.

The app reads [`mods.json`](mods.json) from this repo:

```
https://raw.githubusercontent.com/Dullfin/gtw-mod-index/main/mods.json
```

## Adding your mod

1. Publish your mod as a **GitHub release** in your own repo. Attach a `.zip` or `.dll`.
   - In a zip, any of these layouts work: `BepInEx/plugins/YourMod/...`, `plugins/YourMod/...`, or just your DLL(s) at the root.
   - Don't bundle BepInEx itself. The manager installs it separately.
2. Open a pull request that adds an entry to `mods.json`:

```json
{
  "id": "com.you.yourmod",
  "name": "Your Mod",
  "author": "you",
  "description": "One or two sentences about what it does.",
  "homepage": "https://github.com/you/YourMod",
  "repo": "you/YourMod",
  "asset": "YourMod-*.zip",
  "tags": ["practice"],
  "dependencies": []
}
```

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Unique. Use your `[BepInPlugin]` GUID. |
| `name` | yes | |
| `repo` | yes* | `owner/name` on GitHub. The newest non-prerelease release is used. |
| `asset` | no | Release file to download, `*` wildcards allowed. Default: the first `.zip`, else the first `.dll`. |
| `author`, `description`, `homepage`, `tags` | no | Shown in the app. |
| `dependencies` | no | `id`s of other mods in this list. They're installed first. |
| `downloadUrl`, `version`, `sha256` | no* | Use instead of `repo` for a fixed file hosted elsewhere. `sha256` is checked after download. |

\* Each entry needs either `repo` or `downloadUrl`.

A check runs on every pull request to make sure the file is valid JSON, ids are unique, and required fields are present.

## Safety

Mods run with the same access to your computer as the game. Entries are reviewed before merging, but only install mods you trust.
