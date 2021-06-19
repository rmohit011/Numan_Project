import cProfile
import pandas as pd
import unittest
import sys
from Task1 import task1
import pstats
import io

def task2():
    df_detail_down= pd.read_csv('detail.csv')
    df_detail_down['Absolute Time'] = pd.to_datetime(df_detail_down['Absolute Time'])
    df_detail_down = df_detail_down.resample('60s', on='Absolute Time').sum()

    a=df_detail_down.to_csv("detailDownsampled.csv",index=False)
    df_detail_vol_down = pd.read_csv('detailVol.csv')
    df_detail_vol_down['Realtime'] = pd.to_datetime(df_detail_vol_down['Realtime'])
    df_detail_vol_down = df_detail_vol_down.resample('60s', on='Realtime').sum()

    a=df_detail_vol_down.to_csv("detailVolDownsampled.csv",index=False)
    df_detail_temp_down = pd.read_csv('detailTemp.csv')
    df_detail_temp_down['Realtime'] = pd.to_datetime(df_detail_temp_down['Realtime'])
    df_detail_temp_down = df_detail_temp_down.resample('60s', on='Realtime').sum()

    a=df_detail_temp_down.to_csv("detailTempDownsampled.csv",index=False)
    return [df_detail_down.shape,df_detail_vol_down.shape,df_detail_temp_down.shape]

def cprofile():
    pr = cProfile.Profile()
    pr.enable()
    my_result = task2()
    print(my_result)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()
    with open('cprofile_task2.txt', 'w+') as f:
        f.write(s.getvalue())


class unit_test(unittest.TestCase):
    def test_task2(self):
        try:
            b = task2()
            self.assertEqual(b, [(7643, 8), (7643, 3), (7643, 3)])
        except Exception as e:
            print(e)


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    b=cprofile()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    with open('unit_test_task2.out', 'w') as f:
        main(f)