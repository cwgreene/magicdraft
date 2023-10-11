# Magic Draft Page

# Data Types / Messages
```java
struct DraftState {
    uuid id; // Draft Id
    Seed seed; // Seed for Draft
    List<Players> players; // Players
    List<Set<Card>> originalPacks; // Original Packs
    bool started; // Has draft started?

    // Mutable State here, initially empty
    Map<Player, Set<Card>> playerSelections;
    Map<Player, List<Pack>> playerPacks;
};
```

```java
struct Player{
    uuid playerId;
    String Name;
};
```

```java
struct Pack {
    int packId;
    List<Card> card;
}
```

```java
struct JoinDraft {
    int drafId;
    String playerName;
}
```

```c
struct DraftUpdate {
    int cardId; // Card Id Chosen
    int packId; // Index from Original Pack
    int packState; // Validation that the pack is in the expected state
    int playerId; // player requesting change [SECURE]

}
```

# API Endpoints:

1. `/api/v1/make_draft`
input:
    1. number of players
    2. sets to draft from
    3. addtional draft rules
resp: Draft Json

1. `/api/v1/get_draft?id=draft_id`
input:
1. draft_id
resp:
```json
{
    "draft": {

    }
}
```

1. `/api/v1/update_draft`
input:
1. Draft Id
2. DraftUpdate Object
resp:
Updated Draft state

1. `/api/v1/join_draft`
input:
draft id.
draft join object
Response:
