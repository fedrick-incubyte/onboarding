import MockAdapter from 'axios-mock-adapter'
import { apiClient } from './axiosInstance'
import { getTasks, createTask, updateTask } from './taskService'

const mock = new MockAdapter(apiClient)
afterEach(() => mock.reset())

it('should_fetch_tasks_from_tasks_endpoint', async () => {
  mock.onGet('/tasks').reply(200, [{ id: 1, title: 'Buy milk' }])
  expect(await getTasks()).toEqual([{ id: 1, title: 'Buy milk' }])
})

it('should_post_new_task_to_tasks_endpoint', async () => {
  mock.onPost('/tasks').reply(201, { id: 2, title: 'Walk dog' })
  expect(await createTask({ title: 'Walk dog' })).toMatchObject({ id: 2, title: 'Walk dog' })
})

it('should_put_to_tasks_id_endpoint', async () => {
  mock.onPut('/tasks/2').reply(200, { id: 2, title: 'Walk cat' })
  expect(await updateTask(2, { title: 'Walk cat' })).toMatchObject({ id: 2, title: 'Walk cat' })
})
