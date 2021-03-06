{
  "width": 230,
  "height": 200,
  "padding": {
    "top": 10,
    "left": 80,
    "bottom": 60,
    "right": 10
  },
  "data": [
    {
      "name": "table",
      "values": [
        {
          "DayOfWeek": "1",
          "countDayOfWeek": "68979"
        },
        {
          "DayOfWeek": "2",
          "countDayOfWeek": "80450"
        },
        {
          "DayOfWeek": "3",
          "countDayOfWeek": "84995"
        },
        {
          "DayOfWeek": "4",
          "countDayOfWeek": "87425"
        },
        {
          "DayOfWeek": "5",
          "countDayOfWeek": "69996"
        },
        {
          "DayOfWeek": "6",
          "countDayOfWeek": "53785"
        },
        {
          "DayOfWeek": "7",
          "countDayOfWeek": "63889"
        } 
      ]
    }
  ],
  "scales": [
    {
      "name": "x",
      "type": "ordinal",
      "range": "width",
      "domain": {
        "data": "table",
        "field": "data.DayOfWeek"
      }
    },
    {
      "name": "y",
      "range": "height",
      "nice": true,
      "domain": {
        "data": "table",
        "field": "data.countDayOfWeek"
      }
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "title": "Day of Week",
      "offset": 3,
      "tickSize": 0,
      "properties": {
        "axis": {
          "stroke": {
            "value": "transparent"
          }
        }
      }
    },
    {
      "type": "y",
      "scale": "y",
      "title": "Number of Flights",
      "titleOffset": 55,
      "offset": 3,
      "ticks": 4,
      "tickSize": 0,
      "grid": true,
      "properties": {
        "grid": {
          "stroke": {
            "value": "white"
          },
          "strokeWidth": {
            "value": 2
          }
        },
        "axis": {
          "stroke": {
            "value": "transparent"
          }
        }
      }
    }
  ],
  "marks": [
    {
      "type": "rect",
      "from": {
        "data": "table"
      },
      "properties": {
        "enter": {
          "x": {
            "scale": "x",
            "field": "data.DayOfWeek"
          },
          "width": {
            "scale": "x",
            "band": true,
            "offset": -2
          },
          "y": {
            "scale": "y",
            "field": "data.countDayOfWeek"
          },
          "y2": {
            "scale": "y",
            "value": 0
          }
        },
        "update": {
          "fill": {
            "value": "#31a354"
          }
        },
        "hover": {
          "fill": {
            "value": "#a1d99b"
          }
        }
      }
    }
  ]
}
