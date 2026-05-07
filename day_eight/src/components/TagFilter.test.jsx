import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TagFilter } from './TagFilter.jsx'

describe('TagFilter', () => {
  it('should render an All badge', () => {
    render(<TagFilter entries={[]} onTagSelect={() => {}} />)
    expect(screen.getByText('All')).toBeInTheDocument()
  })

  it('should render one badge for each unique tag in entries', () => {
    const entries = [
      { tags: ['react', 'js'] },
      { tags: ['react', 'css'] },
    ]
    render(<TagFilter entries={entries} onTagSelect={() => {}} />)
    expect(screen.getByText('react')).toBeInTheDocument()
    expect(screen.getByText('js')).toBeInTheDocument()
    expect(screen.getByText('css')).toBeInTheDocument()
  })

  it('should call onTagSelect with the tag when a tag badge is clicked', async () => {
    const onTagSelect = vi.fn()
    const entries = [{ tags: ['react'] }]
    render(<TagFilter entries={entries} onTagSelect={onTagSelect} />)
    await userEvent.click(screen.getByText('react'))
    expect(onTagSelect).toHaveBeenCalledWith('react')
  })
})
