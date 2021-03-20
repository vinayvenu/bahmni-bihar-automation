select 'CBC Tests ordered', count(distinct s.id) as ordered_tests
from analysis a
inner join result r on a.id = r.analysis_id
inner join sample_item si on a.sampitem_id = si.id
inner join sample s on si.samp_id = s.id
inner join test t on a.test_id = t.id
where t.description = 'Haemoglobin (Blood)'
  and date(s.entered_date) = '2021-03-19'
union
select 'CBC Tests done', count(distinct s.id) as ordered_tests
from analysis a
         inner join result r on a.id = r.analysis_id
         inner join sample_item si on a.sampitem_id = si.id
         inner join sample s on si.samp_id = s.id
         inner join test t on a.test_id = t.id
where t.description = 'Haemoglobin (Blood)'
  and date(s.entered_date) = '2021-03-19'
and r.value is not null;
