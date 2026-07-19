# Type: bitfield

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

A value combining several binary flags into one number; the flags can be inspected individually using bitlib functions. For example (using [`GetItemFamily`](../categories/Container.md#getitemfamily) and related constants):

```lua
 GetItemFamily("Crystallized Air") 
 -- returns 1224
 bit.bor(0x0008,0x0040,0x0080,0x0400)
 -- returns 1224
 -- these are the masks for Leatherworking, Enchanting, Engineering, and Mining bags

 bit.band(GetItemFamily("Crystallized Air"), 0x0040)
 -- returns 64, or 0x0040: the item fits in an Enchanting Bag
 bit.band(GetItemFamily("Crystallized Air"), 0x0020)
 -- returns 0, or 0x0040: the item does not fit in an Herb Bag
```

---

← [API Types](../API Types.md)
