import math

print("======================================")
print("      HALF-WAVE RECTIFIER CALCULATOR")
print("======================================")
vrms = float(input("Enter AC input RMS voltage (V): "))
resistance = float(input("Enter load resistance (Ohms): "))

if vrms <= 0 or resistance <= 0:
    print("\nPlease enter positive values.")
else:
    vm = math.sqrt(2) * vrms
    vdc = vm / math.pi
    vout_rms = vm / 2
    idc = vdc / resistance
    irms = vout_rms / resistance
    efficiency = (idc ** 2 * resistance) / (irms ** 2 * resistance) * 100
    ripple_factor = math.sqrt((irms / idc) ** 2 - 1)

    print("\n----------- RESULTS -----------")
    print(f"Peak Voltage       : {vm:.2f} V")
    print(f"DC Output Voltage  : {vdc:.2f} V")
    print(f"RMS Output Voltage : {vout_rms:.2f} V")
    print(f"DC Load Current    : {idc:.4f} A")
    print(f"RMS Load Current   : {irms:.4f} A")
    print(f"Efficiency         : {efficiency:.2f}%")
    print(f"Ripple Factor      : {ripple_factor:.2f}")
    print("-------------------------------")
