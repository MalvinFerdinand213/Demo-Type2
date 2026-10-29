"""Penghubung ke model skoring aspek (Qwen3-VL zero-shot) milikmu.

Isi score_review() dengan pemanggilan modelmu. Kontraknya:
  - text   : str, isi review (boleh kosong kalau ada foto)
  - images : list[bytes], foto review (boleh kosong)
  - star   : int 1-5, bintang hotel
  - return : dict {nama_aspek: skor 1.0-5.0, atau None kalau aspek tidak disebut}
             nama_aspek harus persis salah satu dari hotel_core.ASPECTS

Kalau modelmu mengeluarkan sentimen -1..+1, ubah ke skala 1-5 dengan: skor = 3 + 2 * sentimen
Kalau mengeluarkan label negatif/netral/positif: negatif=1, netral=3, positif=5 (atau sesuai skalamu).
"""
import hashlib
import random

from hotel_core import ASPECTS


def demo_scores(text: str, images: list, star: int) -> dict:
    """Skor DUMMY (bukan dari modelmu), supaya alur app bisa dicoba dulu."""
    key = f"{text}|{len(images)}|{star}".encode()
    rng = random.Random(int(hashlib.sha256(key).hexdigest(), 16) % (2**32))
    return {a: round(min(5.0, max(1.0, rng.gauss(2.2 + 0.4 * star, 0.9))), 1) for a in ASPECTS}


def score_review(text: str, images: list, star: int) -> dict:
    raise NotImplementedError(
        "Isi score_review() di aspect_adapter.py dengan pemanggilan Qwen3-VL milikmu, "
        "atau nyalakan Mode demo di sidebar."
    )
