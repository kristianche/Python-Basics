skumriq_price = float(input())
caca_price = float(input())
palamud_kilos = float(input())
safrid_kilos = float(input())
midi_kilos = int(input())
palamud_price = skumriq_price + (0.60 * skumriq_price)
safrid_price = caca_price + (0.80 * caca_price)
midi_total_price = midi_kilos * 7.50
palamud_total_price = palamud_price * palamud_kilos
safrid_total_price = safrid_price * safrid_kilos
total_price = palamud_total_price + safrid_total_price + midi_total_price
print(f"{total_price:.2f}")