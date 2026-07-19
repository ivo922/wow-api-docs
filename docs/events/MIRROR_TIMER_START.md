# MIRROR_TIMER_START

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MIRROR_TIMER_START)

---

Fires when a special countdown timer starts. Mirror timers are used for breath and fatigue when swimming and for the hunter Feign Death ability.

**Signature:**

```lua
("name", value, maxvalue, step, pause, "label")
```

**Arguments:**

- `name` - The name of the timer that is starting. (`string`)
- `value` - The current value of the timer. (`number`)
- `maxvalue` - The max value of the timer. (`number`)
- `step` - The step that the value moves. (`number`)
- `pause` - Signifies whether the timer is paused. (`number`)
- `label` - The label for the timer. (`string`)
