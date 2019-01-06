import math

class Node :

    def __init__ (self, value) :
        self.value = value
        self.right = None
        self.left = None

    def add (self, node) :
        if (node.value < self.value) :
            if self.left is None :
                self.left = node
            else :
                self.left.add(node)
        elif (node.value > self.value) :
            if self.right is None :
                self.right = node
            else :
                self.right.add(node)
        else :
            return 0

class Tree :

    def __init__ (self, tab) :

        temp = self.sort(tab)

        for i in range (0, len(temp)) :

            if i == 0 :
                self.root = Node(temp[i])
            else :
                self.root.add(Node(temp[i]))


        self.current = self.root
        self.step = 0
        self.height = 0


    def getMiddle (self, tab) :
        if len(tab) % 2 == 0 :
            index = int(len(tab) / 2) - 1
        else :
            index = math.ceil(len(tab) / 2) - 1
        return index


    def sort (self, tab) :

        output = []
        a = []
        b = []
        temp = sorted(tab[:])

        while len(temp) > 0 :

            # On extrait le milieu
            index = self.getMiddle(temp)

            output.append(temp[index])

            # Coupe du tableau
            a = temp[:index]
            b = temp[index+1:]

            # On supprime le milieu initial
            del temp[index]

            # On ajoute les milieux des deux tableaux coupés
            if len(a) > 0 :
                index_a = self.getMiddle(a)
                output.append(a[index_a])
                del temp[temp.index(a[index_a])]

            if len(b) > 0 :
                index_b = self.getMiddle(b)
                output.append(b[index_b])
                del temp[temp.index(b[index_b])]

        return output

    def getStep (self) :
        step = self.step
        self.step = 0
        return step

    def search (self, value) :

        if self.step > self.height :
            self.height = self.step

        if self.current.value == value :
            v = self.current.value
            self.current = self.root
            return v
        elif self.current.value < value :

            if self.current.right is not None :
                self.current = self.current.right
                self.step += 1
                return self.search(value)
            else :
                return 0

        elif self.current.value > value :
            if self.current.left is not None :
                self.current = self.current.left
                self.step += 1
                return self.search(value)
            else :
                return 0

tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

for i in range (1, 26) :
    print (tree.search(i), "trouvé en", tree.getStep(), "itérations.")
print ("Hauteur de l'arbre :", tree.height)
