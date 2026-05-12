import { validateTask } from './task'

it('should_throw_when_title_is_empty', () => {
  expect(() => validateTask({ title: '' })).toThrow('Title is required')
})
