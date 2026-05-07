import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Toggle } from './Toggle.jsx'

describe('Toggle', () => {
  it('should call onToggle when clicked', async () => {
    const onToggle = vi.fn()
    render(<Toggle onToggle={onToggle} />)
    await userEvent.click(screen.getByRole('switch'))
    expect(onToggle).toHaveBeenCalledOnce()
  })

  it('should have aria-checked true when checked is true', () => {
    render(<Toggle checked={true} onToggle={() => {}} />)
    expect(screen.getByRole('switch')).toHaveAttribute('aria-checked', 'true')
  })
})
