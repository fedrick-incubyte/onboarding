import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { EntryCard } from './EntryCard.jsx'

const entry = {
  id: '1',
  title: 'My Learning',
  body: 'I learned TDD today',
  tags: ['tdd', 'react'],
  createdAt: '2024-01-15T10:30:00.000Z',
}

describe('EntryCard', () => {
  it('should render the entry title', () => {
    render(<EntryCard entry={entry} />)
    expect(screen.getByText('My Learning')).toBeInTheDocument()
  })

  it('should render each tag as a Badge', () => {
    render(<EntryCard entry={entry} />)
    expect(screen.getByText('tdd')).toBeInTheDocument()
    expect(screen.getByText('react')).toBeInTheDocument()
  })
})
