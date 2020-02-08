import os
import xlsxwriter

import string

def _add_table(data: dict, data_table, worksheet):
  letters: list = list(string.ascii_lowercase)
  letters = list(map(lambda xi: xi.upper(), letters))

  start_letter = letters[1]
  end_letter = letters[len(data.keys()) + 1]

  start_offset: int = 3
  end_offset: int = start_offset + len(data.keys())

  
  pos_table = f"{start_letter}{start_offset}:${end_letter}${end_offset}"

  def map_2_column(column_name):
    return \
      {
        'header': column_name,
        'total_function': 'average',
      }

  columns = list(map(lambda xi: map_2_column(xi), data.keys()))
  
  worksheet.add_table(
    pos_table,
    {
      'data': data_table,
      'total_row': 1,
      'columns': columns}
    )


  return start_letter, start_offset, end_letter, end_offset

def _create_rows(data: dict):
  

  max_len = max(list(map(lambda xi: len(xi), data.values())))

  tmp_list = [ [] for _ in range(max_len)]

  for k, v in data.items():
    for ii, xi in enumerate(v):
      tmp_list[ii].append(xi)

  return tmp_list

def _fill_table(data: dict, worksheet):
  data_table = _create_rows(data)
  start_letter, start_offset, end_letter, end_offset = \
    _add_table(data, data_table, worksheet)
  pass


def create_table_metrics(data, base_dir_spredsheets: str = './results/spredsheets'):
  path_workbook: str = \
    os.path.join(
      # base_dir_spredsheets,
      '.',
      'test.xlsx'
    )
  if os.path.isdir(base_dir_spredsheets) == False:
    os.makedirs(base_dir_spredsheets)
  
  workbook = xlsxwriter.Workbook(f'{path_workbook}')

  worksheet = workbook.add_worksheet(name='metrics_result')

  _fill_table(data, worksheet)

  workbook.close()

  pass