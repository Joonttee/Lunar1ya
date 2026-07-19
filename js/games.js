    /* ===== Данные: список игр =====
       Чтобы добавить игру — добавьте объект в массив GAMES:
       { title: "Название", genre: "Экшены", year: 2024, status: "playing", tags: ["coop"] }
       status: new | playing | done | planned ; tags: mp | coop (необязательно)
       cover: "covers/name.jpg" (необязательно; без него — цветная заглушка) */
    const GAMES = [
      // Импорт из публичного профиля Rankone: https://www.rankone.global/lunahoomalu
      // Взяты видимые игры (избранное + показанные отзывы). Жанры/статусы — лучшая догадка, правьте под себя.
      { title: "Constance",                genre: "Инди",               year: 2025, status: "done",     tags: []},
      { title: "Grime II",                 genre: "Экшены",             year: 2026, status: "done",     tags: []},
      { title: "RV There Yet?",            genre: "Казуальные",         year: 2025, status: "done",     tags: ["coop"]},
      { title: "Peak",                     genre: "Казуальные",         year: 2025, status: "done",     tags: ["coop"]},
      { title: "Valorant",                 genre: "Экшены",             year: 2020, status: "playing",  tags: ["mp"]},
      { title: "Hollow Knight",            genre: "Приключения",        year: 2017, status: "done",     tags: []},
      { title: "Hollow Knight: Silksong",  genre: "Приключения",        year: 2025, status: "done",     tags: []},
      { title: "Replaced",                 genre: "Экшены",             year: 2023, status: "done",     tags: []},
      // В планах (добавлено вручную):
      { title: "Little Misfortune",         genre: "Приключения",        year: 2019, status: "planned",  tags: []},
      { title: "Bendy and the Ink Factory", genre: "Экшены",             year: 2026, status: "planned",  tags: []}, // Steam: TBA / coming soon
      { title: "Cult of the Lamb",          genre: "Экшены",             year: 2022, status: "planned",  tags: [] },
      { title: "Portal 2",                  genre: "Головоломки",        year: 2011, status: "planned",  tags: [] },
      { title: "Split Fiction",             genre: "Приключения",        year: 2025, status: "planned",  tags: ["coop"] },
      { title: "Little Nightmares II",      genre: "Приключения",        year: 2021, status: "planned",  tags: ["coop"] },
      { title: "Stardew Valley",            genre: "Симуляторы",         year: 2016, status: "planned",  tags: ["coop"] },
      { title: "The Last of Us Part I",     genre: "Экшены",             year: 2022, status: "planned",  tags: [] },
      { title: "Outlast",                   genre: "Экшены",             year: 2013, status: "planned",  tags: [] },
      // В процессе (добавлено вручную):
      { title: "Metro: Last Light Redux",   genre: "Экшены",             year: 2019, status: "playing",  tags: [] },
      { title: "Stray",                     genre: "Приключения",        year: 2022, status: "playing",  tags: [] },
      // Пройдены (добавлено вручную):
      { title: "Moomintroll: Winter's Warmth", genre: "Приключения",    year: 2024, status: "done",     tags: [] },
      { title: "Little Nightmares",            genre: "Приключения",    year: 2017, status: "done",     tags: [] },
      { title: "Little Nightmares III",        genre: "Приключения",    year: 2025, status: "done",     tags: ["coop"] },
      { title: "Resident Evil Requiem",        genre: "Экшены",          year: 2026, status: "done",     tags: [] },
      { title: "Scam Line",                    genre: "Инди",            year: 2024, status: "done",     tags: [] },
      // Пройдены (добавлено вручную, продолжение) — годы/жанры сверены по Steam:
      { title: "Fran Bow",                      genre: "Приключения",    year: 2015, status: "done",     tags: [] },
      { title: "The Past Within",               genre: "Приключения",    year: 2022, status: "done",     tags: ["coop"] },
      { title: "Creepy Tale",                   genre: "Приключения",    year: 2020, status: "done",     tags: [] },
      { title: "The Mortuary Assistant",        genre: "Приключения",    year: 2022, status: "done",     tags: [] },
      { title: "We Were Here",                  genre: "Экшены",          year: 2017, status: "done",     tags: ["coop"] },
      { title: "We Were Here Too",              genre: "Приключения",    year: 2018, status: "done",     tags: ["coop"] },
      { title: "We Were Here Together",         genre: "Приключения",    year: 2019, status: "done",     tags: ["coop"] },
      { title: "We Were Here Forever",          genre: "Приключения",    year: 2021, status: "done",     tags: ["coop"] },
      { title: "Escape the Backrooms",          genre: "Экшены",          year: 2025, status: "done",     tags: ["coop"] },
      { title: "Mafia II: Definitive Edition",  genre: "Экшены",          year: 2020, status: "done",     tags: [] },
      { title: "Mafia: Definitive Edition",     genre: "Экшены",          year: 2020, status: "done",     tags: [] },
      { title: "Reanimal",                      genre: "Приключения",    year: 2026, status: "done",     tags: [] },
      { title: "We Were Here Expeditions: The FriendShip", genre: "Приключения", year: 2023, status: "done", tags: ["coop"] },
      { title: "Call of the Sea",               genre: "Приключения",    year: 2020, status: "done",     tags: [] },
      { title: "Labyrinthine",                  genre: "Экшены",          year: 2023, status: "done",     tags: ["coop"] },
      { title: "Better Mart Simulator",         genre: "Симуляторы",      year: 2025, status: "done",     tags: [] },
      { title: "Lost in Play",                  genre: "Приключения",    year: 2022, status: "done",     tags: [] },
      { title: "There Is No Game",              genre: "Приключения",    year: 2020, status: "done",     tags: [] },
      { title: "It Takes Two",                  genre: "Экшены",          year: 2021, status: "done",     tags: ["coop"] },
      { title: "The Last Campfire",             genre: "Приключения",    year: 2021, status: "done",     tags: [] },
      { title: "Metro 2033 Redux",              genre: "Экшены",          year: 2014, status: "done",     tags: [] }
    ];

    /* Брендовые обложки: сгенерированные иллюстрации + SVG-обложки в едином стиле. */
    const COVER_ART = {
      "Constance": "assets/covers/constance.jpg",
      "Grime II": "assets/covers/grime-ii.jpg",
      "RV There Yet?": "assets/covers/rv-there-yet.jpg",
      "Peak": "assets/covers/peak.jpg",
      "Valorant": "assets/covers/valorant.jpg",
      "Hollow Knight": "assets/covers/hollow-knight.jpg",
      "Hollow Knight: Silksong": "assets/covers/hollow-knight-silksong.jpg",
      "Replaced": "assets/covers/replaced.jpg",
      "Little Misfortune": "assets/covers/little-misfortune.svg",
      "Bendy and the Ink Factory": "assets/covers/bendy-and-the-ink-factory.jpg",
      "Cult of the Lamb": "assets/covers/cult-of-the-lamb.jpg",
      "Portal 2": "assets/covers/portal-2.jpg",
      "Split Fiction": "assets/covers/split-fiction.svg",
      "Little Nightmares II": "assets/covers/little-nightmares-ii.jpg",
      "Stardew Valley": "assets/covers/stardew-valley.jpg",
      "The Last of Us Part I": "assets/covers/the-last-of-us-part-i.jpg",
      "Outlast": "assets/covers/outlast.jpg",
      "Metro: Last Light Redux": "assets/covers/metro-last-light-redux.jpg",
      "Stray": "assets/covers/stray.jpg",
      "Moomintroll: Winter's Warmth": "assets/covers/moomintroll-winters-warmth.svg",
      "Little Nightmares": "assets/covers/little-nightmares.svg",
      "Little Nightmares III": "assets/covers/little-nightmares-iii.svg",
      "Resident Evil Requiem": "assets/covers/resident-evil-requiem.jpg",
      "Scam Line": "assets/covers/scam-line.svg",
      "Fran Bow": "assets/covers/fran-bow.svg",
      "The Past Within": "assets/covers/the-past-within.svg",
      "Creepy Tale": "assets/covers/creepy-tale.svg",
      "The Mortuary Assistant": "assets/covers/the-mortuary-assistant.svg",
      "We Were Here": "assets/covers/we-were-here.svg",
      "We Were Here Too": "assets/covers/we-were-here-too.svg",
      "We Were Here Together": "assets/covers/we-were-here-together.svg",
      "We Were Here Forever": "assets/covers/we-were-here-forever.svg",
      "Escape the Backrooms": "assets/covers/escape-the-backrooms.svg",
      "Mafia II: Definitive Edition": "assets/covers/mafia-ii-definitive-edition.svg",
      "Mafia: Definitive Edition": "assets/covers/mafia-definitive-edition.svg",
      "Reanimal": "assets/covers/reanimal.svg",
      "We Were Here Expeditions: The FriendShip": "assets/covers/we-were-here-expeditions-the-friendship.svg",
      "Call of the Sea": "assets/covers/call-of-the-sea.svg",
      "Labyrinthine": "assets/covers/labyrinthine.svg",
      "Better Mart Simulator": "assets/covers/better-mart-simulator.svg",
      "Lost in Play": "assets/covers/lost-in-play.svg",
      "There Is No Game": "assets/covers/there-is-no-game.svg",
      "It Takes Two": "assets/covers/it-takes-two.jpg",
      "The Last Campfire": "assets/covers/the-last-campfire.svg",
      "Metro 2033 Redux": "assets/covers/metro-2033-redux.svg",
    };

export { GAMES, COVER_ART };
