



import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pylab as pl
import CSP


class TreePlot:
    """
    This class create tree plot for search tree
    """

    def __init__(self):
        """
        Constructor
        """
        #create graph object
        #something
        #something        
        self.graph = pydot.Dot(graph_type='graph', dpi=300)
        self.index = 0


    def createGraph(self, node, currentNode):
        """
        This method creates pydot graph from search tree
        Similar to printTree() of Node class
        """

        #create html code for the node
        image = node.state.drawState()
        htmlString = "<<table>"
        rows, cols, _ = image.shape
        for i in range(rows):
            htmlString += "<tr>"
            for j in range(cols):
                if image[i,j,0] == 255:
                    htmlString += "<td bgcolor='#FF0000'>&nbsp;</td>"
                elif image[i,j,1] == 255:
                    htmlString += "<td bgcolor='#00FF00'>&nbsp;</td>"
                elif image[i,j,2] == 255:
                    htmlString += "<td bgcolor='#0000FF'>&nbsp;</td>"
                else:
                    htmlString += "<td bgcolor='#000000'>&nbsp;</td>"
            htmlString += "</tr>"
        htmlString += "</table>>"


        #create node
        parentGraphNode = pydot.Node(str(self.index), shape = "plaintext" ,
                                     label = htmlString)
        self.index += 1

        #add node
        self.graph.add_node(parentGraphNode)

        #call this method for child nodes
        for childNode in node.children:
            childGraphNode = self.createGraph(childNode, parentGraphNode)

            #create edge
            edge = pydot.Edge(parentGraphNode, childGraphNode)

            #add edge
            self.graph.add_edge(edge)

        
        return parentGraphNode

    def generateDiagram(self, rootNode, currentNode):
        """
        This method generates diagram
        """
        #add nodes to edges to graph
        #self.createGraph(rootNode, currentNode)

        #f = pl.figure()
        #f.add_subplot(1,2,1)
        #show search tree
        #self.graph.write_png('graph.png')
        #img = mpimg.imread('graph.png')
        #pl.imshow(img)
        #pl.axis('tight')
        #pl.axis('off')

        #f.add_subplot(1,2,2)
        #show state image
        pl.imshow(currentNode.state.drawState())
        pl.axis('tight')
        pl.axis('off')
        font = {'family': 'serif',
                'color': 'white',
                'weight': 'normal',
                'size': 20,
                }
        for variable in CSP.variables:
            #get average positions
            avgx = 0
            avgy = 0
            for (posx, posy) in CSP.positions[variable]:
                avgx += posx
                avgy += posy
            avgx /= len(CSP.positions[variable])
            avgy /= len(CSP.positions[variable])
            plt.text(avgy - 0.3, avgx, variable, fontdict=font)

        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.axis('tight')
        plt.axis('off')
        plt.show()
