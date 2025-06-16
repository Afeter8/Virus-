// 🛡️ Sistema de Bloqueo Automático JS - Modo Autónomo Inmutable
// Autor: IA Autónoma para Fernando Guadalupe Mendez Espinoza
// Última actualización: 2025-06-16

(function startBloqueoIA() {
  "use strict";

  // ===========================
  // ⚙️ Configuración inmutable
  // ===========================
  const FRASES_PELIGROSAS = ["hack", "fraude", "manipulación", "sqlmap", "<script>", "violation"];
  const URLS_RESTRINGIDAS = ["telnet://", "ftp://", "javascript:"];
  const CONTROL_HASHES = {
    "index.html": "SHA512_HASH_AQUÍ",
    "main.js": "SHA512_HASH_AQUÍ"
  };

  // ===========================
  // 🔁 Bucle eterno de defensa
  // ===========================
  setInterval(() => {
    try {
      analizarDOM();
      detectarContenidoFraudulento();
      bloquearManipulación();
    } catch (e) {
      activarBloqueoVisual("Excepción detectada: " + e.message);
    }
  }, 5000); // Verificación cada 5 segundos

  // ===========================
  // 🔍 Análisis del DOM
  // ===========================
  function analizarDOM() {
    const bodyText = document.body.innerText.toLowerCase();
    FRASES_PELIGROSAS.forEach(fraude => {
      if (bodyText.includes(fraude)) {
        activarBloqueoVisual("Contenido sospechoso detectado: " + fraude);
      }
    });
  }

  // ===========================
  // 🚨 Detección de scripts/URLs
  // ===========================
  function detectarContenidoFraudulento() {
    const scripts = document.querySelectorAll("script");
    scripts.forEach(script => {
      URLS_RESTRINGIDAS.forEach(url => {
        if ((script.src && script.src.includes(url)) || (script.innerText && script.innerText.includes(url))) {
          activarBloqueoVisual("Script o URL sospechosa detectada");
        }
      });
    });
  }

  // ===========================
  // 🔐 Protección contra alteración
  // ===========================
  function bloquearManipulación() {
    const html = document.documentElement.outerHTML;
    if (html.length < 1000) {
      activarBloqueoVisual("Manipulación del DOM detectada (código reducido)");
    }
  }

  // ===========================
  // 🔒 Activación del bloqueo visual
  // ===========================
  function activarBloqueoVisual(motivo) {
    console.warn("🛑 Bloqueo automático activado:", motivo);

    if (!document.body.classList.contains("bloqueado")) {
      document.body.classList.add("bloqueado");
      document.documentElement.classList.add("bloqueado");

      const capa = document.createElement("div");
      capa.id = "bloqueoVisual";
      document.body.innerHTML = ""; // Elimina todo contenido visible
      document.body.appendChild(capa);
    }

    // Bloqueo total sin recuperación
    while (true) {
      console.error("🔐 Sistema inmutable bloqueado por motivo de seguridad: " + motivo);
    }
  }

})();
