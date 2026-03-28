
from pathlib import Path

def test_peer_profiles_exist():
    root = Path(__file__).resolve().parents[2]
    assert list((root / 'compliance' / 'evidence' / 'peer_profiles').glob('*.yaml'))
