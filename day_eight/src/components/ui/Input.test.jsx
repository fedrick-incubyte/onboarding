import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Input } from './Input.jsx'

describe('Input', () => {
  it('should render a text input by default', () => {
    render(<Input />)
    expect(screen.getByRole('textbox')).toBeInTheDocument()
  })
})
