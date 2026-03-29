with open('discipulomirim-landing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. Remove Potinho block from cards section ---
start_marker = '\n      <!-- Destaque: Potinho da Ora'
cards_section_end = '\n\n    </div>\n  </section>\n\n\n  <!-- ===================== TESTIMONIALS'

s = content.find(start_marker)
e = content.find(cards_section_end)

if s != -1 and e != -1:
    content = content[:s] + cards_section_end + content[e + len(cards_section_end):]
    print("Removed from cards section")
else:
    print(f"Warning: start={s}, end={e}")

# --- 2. Insert compact Potinho block right after the pricing section ---
pricing_insert_point = '  </section>\n\n\n  <!-- ===================== CTA'

potinho_section = '''  </section>

  <!-- ===================== POTINHO DESTAQUE ===================== -->
  <section class="py-8 bg-white">
    <div class="max-w-4xl mx-auto px-6">
      <div class="rounded-4xl overflow-hidden shadow-[0_8px_40px_rgba(244,63,94,0.2)] border-2 border-rose-200 relative">
        <div class="absolute top-5 left-5 z-20">
          <span class="bg-rose-500 text-white text-xs font-black px-3 py-1 rounded-full uppercase tracking-widest shadow-md animate-pulse">\u2728 Tamb\u00e9m dispon\u00edvel</span>
        </div>
        <div class="flex flex-col md:flex-row">
          <div class="md:w-2/5 bg-gradient-to-br from-pink-400 to-rose-600 flex items-center justify-center p-8 relative overflow-hidden min-h-[200px]">
            <div class="absolute top-4 left-8 text-white/20 text-8xl font-black">\u2736</div>
            <div class="absolute bottom-4 right-6 text-white/15 text-6xl font-black">\u2605</div>
            <div class="relative z-10 drop-shadow-2xl">
              <svg viewBox="0 0 100 110" width="140" height="140" xmlns="http://www.w3.org/2000/svg">
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
          <div class="md:w-3/5 bg-white p-8 md:p-10 flex flex-col justify-center">
            <span class="text-xs font-bold text-rose-600 bg-pink-50 px-3 py-1 rounded-full inline-block w-fit mb-3">Produto separado</span>
            <h3 class="font-black text-gray-900 text-2xl md:text-3xl mb-2 leading-tight">
              Potinho da Ora\u00e7\u00e3o
              <span class="block text-rose-500 text-base md:text-lg font-extrabold">90 ora\u00e7\u00f5es para crian\u00e7as se aproximarem de Deus</span>
            </h3>
            <p class="text-gray-500 font-semibold text-sm leading-relaxed mb-5">
              Imprima, corte e coloque num potinho de vidro. Seu filho pega uma ora\u00e7\u00e3o por dia e aprende a se conectar com Deus com alegria e autonomia.
            </p>
            <div class="flex flex-wrap gap-x-5 gap-y-2 mb-5 text-xs font-bold text-gray-400">
              <span>\u2714 Para imprimir \u00e0 vontade</span>
              <span>\u2714 Acesso imediato</span>
              <span>\u2714 Garantia de 30 dias</span>
            </div>
            <a href="potinho-oracao.html"
               class="inline-block text-center bg-rose-500 text-white font-extrabold py-3 px-8 rounded-3xl
                      shadow-[0_4px_16px_rgba(244,63,94,0.4)] hover:bg-rose-600 hover:scale-105
                      transition-all duration-200 text-sm w-full md:w-auto">
              Conhecer o Potinho \U0001f64f
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ===================== CTA'''

if pricing_insert_point in content:
    content = content.replace(pricing_insert_point, potinho_section, 1)
    print("Inserted near pricing")
else:
    print("Warning: pricing insert point not found")

with open('discipulomirim-landing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
