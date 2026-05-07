import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { EntryGrid } from './EntryGrid.jsx'

const entries = [
  { id: '1', title: 'Entry One', body: 'body', tags: [], createdAt: '' },
  { id: '2', title: 'Entry Two', body: 'body', tags: [], createdAt: '' },
]

describe('EntryGrid', () => {
  it('should render one card for each entry', () => {
    render(<EntryGrid entries={entries} />)
    expect(screen.getByText('Entry One')).toBeInTheDocument()
    expect(screen.getByText('Entry Two')).toBeInTheDocument()
  })
})
