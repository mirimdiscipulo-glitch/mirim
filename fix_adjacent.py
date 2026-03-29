for filename in ['index.html', 'discipulomirim-landing.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Find the potinho section and grab its inner card HTML
    potinho_start = content.find('\n\n  <!-- ===================== POTINHO DESTAQUE')
    potinho_end_marker = '\n\n\n  <!-- ===================== CTA'
    potinho_end = content.find(potinho_end_marker, potinho_start)

    if potinho_start == -1 or potinho_end == -1:
        print(f'{filename}: markers not found, skipping')
        continue

    # Remove the entire Potinho section block
    content_without = content[:potinho_start] + content[potinho_end:]

    # 2. Build compact potinho card (just the card div, no section wrapper)
    potinho_card = '''

      <!-- Potinho da Oração – logo abaixo -->
      <div class="mt-6 rounded-4xl overflow-hidden border-2 border-rose-200 relative shadow-[0_4px_20px_rgba(244,63,94,0.15)]">
        <div class="absolute top-4 left-4 z-20">
          <span class="bg-rose-500 text-white text-xs font-black px-3 py-1 rounded-full uppercase tracking-widest shadow-md">\u2728 Tamb\u00e9m dispon\u00edvel separado</span>
        </div>
        <div class="flex flex-col md:flex-row">
          <div class="md:w-1/3 bg-gradient-to-br from-pink-400 to-rose-600 flex items-center justify-center p-8 relative overflow-hidden min-h-[180px]">
            <div class="absolute top-3 left-6 text-white/20 text-7xl font-black">\u2736</div>
            <div class="absolute bottom-3 right-4 text-white/15 text-5xl font-black">\u2605</div>
            <div class="relative z-10">
              <svg viewBox="0 0 100 110" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
                <rect x="30" y="8" width="40" height="14" rx="4" fill="#A0714F"/>
                <rect x="26" y="18" width="48" height="6" rx="3" fill="#8B5E3C"/>
                <path d="M22 30 Q18 34 18 42 L18 88 Q18 96 26 96 L74 96 Q82 96 82 88 L82 42 Q82 34 78 30 Z" fill="rgba(255,255,255,0.4)" stroke="rgba(255,255,255,0.8)" stroke-width="2"/>
                <path d="M26 36 Q24 50 25 65" stroke="rgba(255,255,255,0.6)" stroke-width="3" fill="none" stroke-linecap="round"/>
                <rect x="32" y="68" width="16" height="18" rx="2" fill="#FFD54F" transform="rotate(-10 32 68)"/>
                <rect x="44" y="65" width="16" height="18" rx="2" fill="#81C784" transform="rotate(5 44 65)"/>
                <rect x="56" y="67" width="14" height="16" rx="2" fill="#FF8A65" transform="rotate(-5 56 67)"/>
                <rect x="38" y="72" width="14" height="15" rx="2" fill="#64B5F6" transform="rotate(8 38 72)"/>
              </svg>
            </div>
          </div>
          <div class="md:w-2/3 bg-white p-7 flex flex-col justify-center">
            <h3 class="font-black text-gray-900 text-xl md:text-2xl mb-1 leading-tight">
              Potinho da Ora\u00e7\u00e3o
              <span class="block text-rose-500 text-sm md:text-base font-extrabold">90 ora\u00e7\u00f5es para crian\u00e7as se aproximarem de Deus</span>
            </h3>
            <p class="text-gray-500 font-semibold text-sm leading-relaxed mb-4 mt-2">
              Imprima, corte e coloque num potinho de vidro. Seu filho pega uma ora\u00e7\u00e3o por dia e aprende a se conectar com Deus.
            </p>
            <div class="flex flex-wrap gap-x-4 gap-y-1 mb-4 text-xs font-bold text-gray-400">
              <span>\u2714 Para imprimir \u00e0 vontade</span>
              <span>\u2714 Acesso imediato</span>
              <span>\u2714 Garantia de 30 dias</span>
            </div>
            <a href="potinho-oracao.html"
               class="inline-block text-center bg-rose-500 text-white font-extrabold py-3 px-8 rounded-3xl
                      shadow-[0_4px_14px_rgba(244,63,94,0.35)] hover:bg-rose-600 hover:scale-105
                      transition-all duration-200 text-sm w-full md:w-auto">
              Conhecer o Potinho \U0001f64f
            </a>
          </div>
        </div>
      </div>'''

    # 3. Insert the card right after the blue pricing card's closing </div></div>
    # The pricing section structure ends with:  </div>\n    </div>\n  </section>
    pricing_section_end = '\n    </div>\n  </section>'
    # Find it after the "preco" id
    preco_pos = content_without.find('id="preco"')
    section_end_pos = content_without.find(pricing_section_end, preco_pos)

    if section_end_pos == -1:
        print(f'{filename}: pricing section end not found')
        continue

    # Insert potinho card + close the section
    content_new = (
        content_without[:section_end_pos] +
        potinho_card +
        content_without[section_end_pos:]
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content_new)

    print(f'{filename}: done')
