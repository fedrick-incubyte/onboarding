import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { DarkModeToggle } from './DarkModeToggle.jsx'

describe('DarkModeToggle', () => {
  it('should call onToggle when the toggle is clicked', async () => {
    const onToggle = vi.fn()
    render(<DarkModeToggle darkMode={false} onToggle={onToggle} />)
    await userEvent.click(screen.getByRole('switch'))
    expect(onToggle).toHaveBeenCalled()
  })
})
