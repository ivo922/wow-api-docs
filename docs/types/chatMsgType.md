# Type: chatMsgType

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

String identifying the common type of a set of chat window messages; used in chat window functions for determining which windows display which messages and the colors used for displaying each message type.

Each `CHAT_MSG_`*X* [event](../Events.md) has a corresponding `chatMsgType`, idendified by the part of the event name following the initial `CHAT_MSG_`; e.g. the `chatMsgType` for [`CHAT_MSG_COMBAT_FACTION_CHANGE`](../events/CHAT_MSG_COMBAT_FACTION_CHANGE.md) is `COMBAT_FACTION_CHANGE`. A list of pre-configured `chatMsgType`s can be found as keys in the global table `ChatTypeInfo`.

---

← [API Types](../API Types.md)
