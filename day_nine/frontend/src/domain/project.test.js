import { validateProject } from './project'

it('should_throw_when_name_is_empty', () => {
  expect(() => validateProject({ name: '' })).toThrow('Name is required')
})
