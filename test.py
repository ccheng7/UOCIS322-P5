import arrow 
import nose
import logging
import acp_times
import sys
logging.basicConfig(format = '%(levelname)s:(message)s',level = logging.WARNING
log = logging.getLogger(__name__)
sys.path.append("..")

def test_brevet_dist_time_200():
    time = arrow.now()
    assert acp_times.open_time(0, 200, time) == time
    assert acp_times.close_time(0, 200, time) == time.shift(hours = 1)
    assert acp_times.open_time(20, 200, time) == time.shift(minutes = 35)
    assert acp_times.close_time(20, 200, time) == time.shift(hours = 2)
    assert acp_times.open_time(60, 200, time) == time.shift(hours =1 , minutes =46)
    assert acp_times.close_time(60, 200, time) == time.shift(hours = 4)


def test_brevet_dist_time_200_db_test():
	time = arrow.now()
	assert acp_times.open_time(0, 200, time) == time
    assert acp_times.close_time(0, 200, time) == time.shift(hours = 1)
    assert acp_times.open_time(20, 200, time) == time.shift(minutes = 35)
    assert acp_times.close_time(20, 200, time) == time.shift(hours = 2)
    #insert into db
    submit_func()
    #show the fucntion
    assert display_func() == render_template('display.html')
    #show delete all of them
    assert delete_function() == render_template('delete_all.html')
    #should display the empty page
    assert display_func() == render_template('lack_input.html')