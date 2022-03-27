
from PyQt5.QtWidgets import QGraphicsPolygonItem
from PyQt5.QtGui import QPolygonF, QBrush, QColor
from PyQt5.QtCore import QPointF, QRandomGenerator
import datetime

class DiagramItem(QGraphicsPolygonItem):
    def __init__(self, diagramType):
        super(DiagramItem, self).__init__()
        if(diagramType == "Box"):
            boxPoligon= QPolygonF([QPointF(0, 0),QPointF(0, 30),QPointF(30, 30),QPointF(30, 0),QPointF(0, 0)])     
            self.setPolygon(boxPoligon)
        else:
            trianglePoligon= QPolygonF([QPointF(15, 0),QPointF(30, 30),QPointF(0, 30),QPointF(15, 0)])
            self.setPolygon(trianglePoligon)
        
        rng =QRandomGenerator(datetime.datetime.now().second)
        color= QColor(rng.bounded(256),rng.bounded(256),rng.bounded(256))
        brush =QBrush(color)
        self.setBrush(brush)

