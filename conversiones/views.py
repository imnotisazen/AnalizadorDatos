
from django.shortcuts import render


def inicio(request):
    contexto = {
        "resultado": None,
        "error": None,
        "texto_resultado": None,
        "error_texto": None,
    }

    if request.method == "POST":
        accion = request.POST.get("accion")

        if accion == "convertir":
            numero = request.POST.get("numero", "").strip()
            base = request.POST.get("base", "10")

            bases = {
                "2": 2,
                "8": 8,
                "10": 10,
                "16": 16,
            }

            digitos = {
                2: "01",
                8: "01234567",
                10: "0123456789",
                16: "0123456789ABCDEF",
            }

            if not numero:
                contexto["error"] = "Debe ingresar un número."

            elif base not in bases:
                contexto["error"] = "La base seleccionada no es válida."

            elif numero.startswith("-"):
                contexto["error"] = "No se permiten números negativos."

            elif any(c not in digitos[bases[base]]
                     for c in numero.upper()):
                contexto["error"] = (
                    "El número contiene dígitos inválidos "
                    "para la base seleccionada."
                )

            else:
                valor = int(numero, bases[base])

                if valor > 65535:
                    contexto["error"] = (
                        "El número está fuera del rango permitido "
                        "(0 a 65535)."
                    )
                else:
                    bits = max(1, valor.bit_length())
                    bytes_necesarios = (bits + 7) // 8
                    bits_completos = bytes_necesarios * 8

                    binario = format(valor, "b").zfill(
                        bits_completos
                    )

                    contexto["resultado"] = {
                        "decimal": valor,
                        "binario": binario,
                        "octal": format(valor, "o"),
                        "hexadecimal": format(valor, "X"),
                        "bits": bits,
                        "bytes": bytes_necesarios,
                        "bits_completos": bits_completos,
                    }

        elif accion == "texto":
            texto = request.POST.get("texto", "")

            if not texto:
                contexto["error_texto"] = (
                    "Debe ingresar un texto."
                )

            elif len(texto) > 20:
                contexto["error_texto"] = (
                    "El texto no puede superar los 20 caracteres."
                )

            else:
                caracteres = []

                for caracter in texto:
                    codigo = ord(caracter)
                    utf8 = caracter.encode("utf-8")

                    caracteres.append({
                        "caracter": caracter,
                        "decimal": codigo,
                        "unicode": f"U+{codigo:04X}",
                        "hexadecimal": f"{codigo:X}",
                        "utf8": " ".join(
                            f"{byte:02X}" for byte in utf8
                        ),
                    })

                contexto["texto_resultado"] = caracteres

    return render(
        request,
        "conversiones/inicio.html",
        contexto
    )
