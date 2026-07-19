import { GAMES, COVER_ART } from "./games.js";

/* ===== Логика интерфейса ===== */
    const STATUS_META = {
      new:     { label: "🆕 Не начато",  cls: "st-new" },
      playing: { label: "⏳ В процессе", cls: "st-playing" },
      done:    { label: "✅ Пройдено",  cls: "st-done" },
      planned: { label: "📌 В планах",   cls: "st-planned" }
    };
    const TAG_META = { mp: "🕹️ MP", coop: "🤝 Coop" };

    const state = { status: "all", genre: "all", era: "all", query: "", sort: "title-asc", view: "grid" };
    const $ = (s) => document.querySelector(s);
    const gamesEl = $("#games");
    const emptyEl = $("#empty");
    const resultCountEl = $("#resultCount");

    function hashString(str) {
      let h = 0;
      for (let i = 0; i < str.length; i++) h = (h * 31 + str.charCodeAt(i)) >>> 0;
      return h;
    }
    function placeholderCover(title) {
      const h = hashString(title);
      const hue1 = h % 360;
      const hue2 = (hue1 + 60 + (h % 120)) % 360;
      const bg = `linear-gradient(135deg, hsl(${hue1} 60% 35%), hsl(${hue2} 65% 22%))`;
      const letter = title.trim().charAt(0).toUpperCase();
      return `<div class="ph-cover" style="background:${bg}">${letter}</div>`;
    }
    function coverFallback(img) {
      const ph = placeholderCover(img.getAttribute("data-title") || "?");
      img.insertAdjacentHTML("afterend", ph);
      img.remove();
    }

    function gameCard(game) {
      const st = STATUS_META[game.status] || STATUS_META.new;
      const tags = (game.tags || []).map((t) => `<span class="g-tag">${TAG_META[t] || t}</span>`).join("");
      const coverPath = game.cover || COVER_ART[game.title];
      const cover = coverPath
        ? `<img class="cover-img" src="${coverPath}" alt="Обложка ${game.title}" data-title="${game.title}" loading="lazy" decoding="async" onerror="coverFallback(this)">`
        : placeholderCover(game.title);
      return `
        <article class="game" data-title="${game.title.toLowerCase()}">
          <div class="cover">${cover}<span class="cover-brand">LUNAR1YA</span><span class="badge ${st.cls}">${st.label}</span></div>
          <div class="info">
            <h3 class="g-title">${game.title}</h3>
            <div class="g-meta"><span>${game.genre}</span><span>${game.year}</span></div>
            <div class="g-tags">${tags}</div>
          </div>
        </article>`;
    }

    function renderStats() {
      const counts = { total: GAMES.length, playing: 0, done: 0, planned: 0 };
      GAMES.forEach((g) => { if (counts[g.status] !== undefined) counts[g.status]++; });
      document.querySelectorAll("#stats [data-stat]").forEach((el) => { el.textContent = counts[el.dataset.stat]; });
    }

    function fillGenres() {
      const genres = [...new Set(GAMES.map((g) => g.genre))].sort((a, b) => a.localeCompare(b, "ru"));
      $("#genreFilter").innerHTML = `<option value="all">Все жанры</option>` + genres.map((g) => `<option value="${g}">${g}</option>`).join("");
    }

    function getFiltered() {
      let list = GAMES.filter((g) => {
        if (state.status === "all") {
          // все
        } else if (["mp", "coop"].includes(state.status)) {
          if (!(g.tags || []).includes(state.status)) return false;
        } else if (g.status !== state.status) {
          return false;
        }
        if (state.genre !== "all" && g.genre !== state.genre) return false;
        if (state.era === "new" && !(g.year >= 2024)) return false;
        if (state.era === "modern" && !(g.year >= 2018 && g.year <= 2023)) return false;
        if (state.era === "retro" && !(g.year < 2018)) return false;
        if (state.query && !g.title.toLowerCase().includes(state.query)) return false;
        return true;
      });
      const cmp = {
        "title-asc":  (a, b) => a.title.localeCompare(b.title, "ru"),
        "title-desc": (a, b) => b.title.localeCompare(a.title, "ru"),
        "year-desc":  (a, b) => b.year - a.year,
        "year-asc":   (a, b) => a.year - b.year
      }[state.sort];
      list.sort(cmp);
      return list;
    }

    function renderSidebarStats(list) {
      const completed = GAMES.filter((g) => g.status === "done").length;
      const percent = GAMES.length ? (completed / GAMES.length) * 100 : 0;
      $("#progressPercent").textContent = `${percent.toFixed(1)}%`;
      $("#progressFill").style.width = `${percent}%`;
      $("#sidebarTotal").textContent = GAMES.length;
      $("#sidebarFiltered").textContent = list.length;

      const genres = Object.entries(GAMES.reduce((counts, game) => {
        counts[game.genre] = (counts[game.genre] || 0) + 1;
        return counts;
      }, {})).sort((a, b) => b[1] - a[1]).slice(0, 3);
      $("#genreList").innerHTML = genres.map(([genre, count]) => {
        const share = (count / GAMES.length) * 100;
        return `<div class="genre-row"><div class="genre-row-head"><b>${genre}</b><span>${share.toFixed(0)}% (${count})</span></div><div class="genre-bar"><i style="width:${share}%"></i></div></div>`;
      }).join("");
    }

    function render() {
      const list = getFiltered();
      gamesEl.dataset.view = state.view;
      gamesEl.innerHTML = list.map(gameCard).join("");
      emptyEl.hidden = list.length !== 0;
      const word = list.length === 1 ? "игра" : (list.length < 5 ? "игры" : "игр");
      resultCountEl.textContent = `Показано: ${list.length} ${word}`;
      renderSidebarStats(list);
    }

    function bindEvents() {
      $("#statusBar").addEventListener("click", (e) => {
        const btn = e.target.closest(".sbtn");
        if (!btn) return;
        $("#statusBar .sbtn").forEach((b) => b.classList.remove("is-active"));
        btn.classList.add("is-active");
        state.status = btn.dataset.status;
        render();
      });
      $("#genreFilter").addEventListener("change", (e) => { state.genre = e.target.value; render(); });
      $("#eraFilter").addEventListener("change", (e) => { state.era = e.target.value; render(); });
      $("#sort").addEventListener("change", (e) => { state.sort = e.target.value; render(); });
      let t;
      $("#search").addEventListener("input", (e) => {
        clearTimeout(t);
        t = setTimeout(() => { state.query = e.target.value.trim().toLowerCase(); render(); }, 120);
      });
      document.querySelectorAll(".vbtn").forEach((b) => {
        b.addEventListener("click", () => {
          document.querySelectorAll(".vbtn").forEach((x) => x.classList.remove("is-active"));
          b.classList.add("is-active");
          state.view = b.dataset.view;
          render();
        });
      });
      $("#reset").addEventListener("click", () => {
        state.status = "all"; state.genre = "all"; state.era = "all"; state.query = ""; state.sort = "title-asc";
        $("#search").value = "";
        $("#genreFilter").value = "all";
        $("#eraFilter").value = "all";
        $("#sort").value = "title-asc";
        $("#statusBar .sbtn").forEach((b) => b.classList.toggle("is-active", b.dataset.status === "all"));
        render();
      });
    }

    document.getElementById("year").textContent = new Date().getFullYear();
    renderStats();
    fillGenres();
    bindEvents();
    render();
