import pcbnew
from pcbnew import VECTOR2I as Vec2, VECTOR2I_MM as Vec2mm

def find_footprint(reference: str):
    board = pcbnew.GetBoard()
    footprints = board.GetFootprints()
    return [f for f in footprints if f.GetReference() == reference][0]

def reposition_diode(refnum: int):
    diode = find_footprint(f"DS{refnum}")
    keyswitch = find_footprint(f"K{refnum}")
    position = keyswitch.GetPosition() - Vec2mm(0, 4.7)
    diode.SetPosition(position)
    pcbnew.Refresh()
