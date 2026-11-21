// All persistence goes through here (IndexedDB). Components must not touch
// IndexedDB or localStorage directly, or offline sync breaks.
export async function saveRecipe(recipe) {
  return recipe
}
