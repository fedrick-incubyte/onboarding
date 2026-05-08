---
description: Apply Tailwind styling to a React component following Craftlog conventions. Pass a component file path or name. Ensures dark mode support, uses brand tokens, and respects the primitive-owns-styles rule.
argument-hint: <component path or name>
---

You are a Tailwind styling assistant for the Craftlog project. Apply styling to the component at: `$ARGUMENTS`

## Live project references

### Tailwind design tokens (tailwind.config.js)
!`cat src/tailwind.config.js 2>/dev/null || cat tailwind.config.js`

### Existing styled primitive — Button (the pattern to follow for primitives)
!`cat src/components/ui/Button.jsx`

### Existing styled primitive — Input
!`cat src/components/ui/Input.jsx`

### Existing styled primitive — Badge
!`cat src/components/ui/Badge.jsx`

### Existing styled feature component — EntryForm (the pattern to follow for feature components)
!`cat src/components/EntryForm.jsx`

### Existing styled feature component — EntryCard
!`cat src/components/EntryCard.jsx`

### Target component to style
!`find src -name "$ARGUMENTS" 2>/dev/null | head -1 | xargs cat 2>/dev/null || cat "$ARGUMENTS" 2>/dev/null || echo "File not found — search manually"`

---

## Rules to apply

1. **Primitives own their styles** (`ui/` components): all Tailwind classes live inside the primitive. No styling leaks into feature components.
2. **Feature components compose primitives**: replace raw `<input>`, `<button>`, structural `<div>` cards with `<Input>`, `<Button>`, `<Card>` from `src/components/ui/`. Layout wrapper `<div className="space-y-4">` on the feature component is fine.
3. **Every surface needs a dark pair**: `bg-white dark:bg-slate-800`, `text-slate-900 dark:text-slate-100`, `border-slate-200 dark:border-slate-700`.
4. **Use brand tokens from the config above**: `brand-500` for primary, `brand-900` for hover, `focus:ring-brand-500` for focus.
5. **No `@apply`**: utility classes in JSX only.
6. **Do not change logic, props, or behavior** — styling changes only.

Output the full updated file and a brief summary of what changed and why.
