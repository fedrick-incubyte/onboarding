export const TASK_STATUS = {
  TODO: 'todo',
  IN_PROGRESS: 'in_progress',
  DONE: 'done',
}

export function validateTask({ title }) {
  if (!title) throw new Error('Title is required')
  if (title.length > 200) throw new Error('Title too long')
}

export function normalizeTask({ title, status, ...rest }) {
  return { title: title.trim(), status: status ?? TASK_STATUS.TODO, ...rest }
}
