import MockAdapter from 'axios-mock-adapter'
import { apiClient } from './axiosInstance'
import { getTasks } from './taskService'

const mock = new MockAdapter(apiClient)
afterEach(() => mock.reset())

it('should_fetch_tasks_from_tasks_endpoint', async () => {
  mock.onGet('/tasks').reply(200, [{ id: 1, title: 'Buy milk' }])
  expect(await getTasks()).toEqual([{ id: 1, title: 'Buy milk' }])
})
