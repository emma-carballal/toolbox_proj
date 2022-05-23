from toolbox_proj.lib import search_songs
import toolbox_proj.api_key

def test_search_songs():
    assert len(search_songs("PJ Harvey")) != 0
