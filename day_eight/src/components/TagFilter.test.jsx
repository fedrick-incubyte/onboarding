import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TagFilter } from './TagFilter.jsx'

describe('TagFilter', () => {
  it('should render an All badge', () => {
    render(<TagFilter entries={[]} onTagSelect={() => {}} />)
    expect(screen.getByText('All')).toBeInTheDocument()
  })
})
