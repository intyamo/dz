from polygon import polygon_vertices


def float_cmp(a: float, b: float):
    return abs(a - b) <= 0.001


def test_hexagon():
    expected = [
        (0.0, 3.0),
        (2.598076211353316, 1.5),
        (2.598076211353316, -1.4999999999999996),
        (8.498308346471969e-16, -3.0),
        (-2.5980762113533156, -1.5000000000000009),
        (-2.598076211353317, 1.4999999999999982),
    ]

    hexagon = polygon_vertices(6)

    assert len(hexagon) == len(expected)

    for (x1, y1), (x2, y2) in zip(hexagon, expected):
        assert float_cmp(x1, x2)
        assert float_cmp(y1, y2)


def test_decagon():
    expected = [
        (0.0, 3.0),
        (1.7633557568774194, 2.4270509831248424),
        (2.8531695488854605, 0.9270509831248421),
        (2.8531695488854605, -0.9270509831248421),
        (1.7633557568774194, -2.4270509831248424),
        (1.8369701987210297e-16, -3.0),
        (-1.7633557568774192, -2.4270509831248424),
        (-2.8531695488854605, -0.9270509831248426),
        (-2.853169548885461, 0.9270509831248419),
        (-1.7633557568774196, 2.427050983124842),
    ]

    decagon = polygon_vertices(10)

    assert len(decagon) == len(expected)

    for (x1, y1), (x2, y2) in zip(decagon, expected):
        assert float_cmp(x1, x2)
        assert float_cmp(y1, y2)
