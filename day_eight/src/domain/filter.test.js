import { describe, it, expect } from 'vitest'
import { filterEntries } from './filter.js'

const entries = [
  { id: '1', title: 'A', body: 'body', tags: ['react', 'js'], createdAt: '' },
  { id: '2', title: 'B', body: 'body', tags: ['css'], createdAt: '' },
  { id: '3', title: 'C', body: 'body', tags: ['react'], createdAt: '' },
]

describe('filterEntries', () => {
  it('should return all entries when tag is null', () => {
    expect(filterEntries(entries, null)).toHaveLength(3)
  })
})
