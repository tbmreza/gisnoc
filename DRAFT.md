
len: int = ffi("octave", "100 * 10")  # octave-cli --quiet --eval 'disp(42)'
peak: double = ffi("octave", "99.5")

class C(n):
    tx = DecoratedField()

record = Consig()
record["tx"] = 20
print(tx)  # set global var...
res = consig.lfilter("tx")  # ...as well as our helper dict

@consig
tx = np.rand(0, peak, len)
record(tx)

consig = ConsigPrelude()
def record(var):
    dict[var.name] = var.value
    write .consig_cache
    

import pyconsig.std as consig
import pyconsig.ffi as ffi
from pyconsig.ffi import record

res = consig.lfilter("tx")  # accesses .consig_cache

ffi : lang -> expr -> value_of_type
foreign pulse
eval expr  python -c 'print("12")'
read fs

lfilter : var -> value
    finds "tx" in .consig_cache
    res = dll.lfilter(tx)

def get_lhs_of_call():
    frame = inspect.currentframe().f_back
    code = inspect.getsource(frame)
    tree = ast.parse(code)