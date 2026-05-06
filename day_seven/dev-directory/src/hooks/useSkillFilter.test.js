import { renderHook, act } from '@testing-library/react';
import { useSkillFilter } from './useSkillFilter';

describe('useSkillFilter', () => {
  it('should return null as the initial active skill', () => {
    const { result } = renderHook(() => useSkillFilter());
    expect(result.current.activeSkill).toBeNull();
  });

  it('should set the active skill when a skill is selected', () => {
    const { result } = renderHook(() => useSkillFilter());
    act(() => result.current.selectSkill('React'));
    expect(result.current.activeSkill).toBe('React');
  });

  it('should clear the active skill when the same skill is selected again', () => {
    const { result } = renderHook(() => useSkillFilter());
    act(() => result.current.selectSkill('React'));
    act(() => result.current.selectSkill('React'));
    expect(result.current.activeSkill).toBeNull();
  });

  it('should clear the active skill when clearFilter is called', () => {
    const { result } = renderHook(() => useSkillFilter());
    act(() => result.current.selectSkill('React'));
    act(() => result.current.clearFilter());
    expect(result.current.activeSkill).toBeNull();
  });
});
