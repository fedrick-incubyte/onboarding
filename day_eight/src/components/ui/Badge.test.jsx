import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Badge } from './Badge.jsx'

describe('Badge', () => {
  it('should render the label text', () => {
    render(<Badge label="react" />)
    expect(screen.getByText('react')).toBeInTheDocument()
  })

  it('should call onClick when clickable and clicked', async () => {
    const onClick = vi.fn()
    render(<Badge label="react" clickable onClick={onClick} />)
    await userEvent.click(screen.getByText('react'))
    expect(onClick).toHaveBeenCalledOnce()
  })
})
