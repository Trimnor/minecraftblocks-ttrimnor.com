import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QFrame, QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Load the background image and check if it's loaded correctly
        background = QPixmap("1577.jpg")
        if background.isNull():
            QMessageBox.critical(self, "Error", "Failed to load background image.")
            sys.exit(1)
        
        # Set the window size to match the image size
        self.setFixedSize(background.size())

        # Set the background
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

        # List of Minecraft blocks and tools
        block_names = [
            "Crafting Table", "Planks", "Stone", "Furnace", "Chest", "Torch",
            "Diamond", "Gold", "Iron", "Emerald", "Redstone", "Lapis Lazuli",
            "Sand", "Gravel", "Dirt", "Cobblestone", "Wood", "Grass Block",
            "Glass", "Brick", "Obsidian", "Netherite", "Bedrock", "Bucket of Water", "Bucket of Lava", "Sword", "Bow", "Arrow", "Shield",
            "Iron Armor", "Diamond Armor", "Netherite Armor", "Enchanting Table"
        ]
        self.buttons = []

        # Create a widget for the left side and add buttons to it
        left_widget = QWidget()
        vbox_left = QVBoxLayout(left_widget)
        for name in block_names:
            button = QPushButton(name, self)
            button.setStyleSheet("background-color: #212121; color: #ffffff; border-radius: 5px; padding: 10px;")
            button.clicked.connect(self.button_clicked)
            self.buttons.append(button)
            vbox_left.addWidget(button)
        
        vbox_left.addStretch(1)

        # Create a QScrollArea for the left side
        scroll_area = QScrollArea()
        scroll_area.setWidget(left_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)

        # Create a horizontal layout to split the two parts
        hbox = QHBoxLayout()

        # The left side will take 30% of the space
        hbox.addWidget(scroll_area, 4)

        # The right side will take 70% of the space
        self.right_label_use = QLabel("Zgjidh një bllok nga e majta...", self)
        self.right_label_use.setStyleSheet("background-color: #f0f0f0; color: #333333; font-size: 20px; padding: 10px; border-radius: 5px;")
        self.right_label_use.setWordWrap(True)
        
        self.right_label_find = QLabel("", self)
        self.right_label_find.setStyleSheet("background-color: #f0f0f0; color: #333333; font-size: 20px; padding: 10px; border-radius: 5px;")
        self.right_label_find.setWordWrap(True)

        self.right_image_label = QLabel(self)
        self.right_image_label.setAlignment(Qt.AlignCenter)

        vbox_right = QVBoxLayout()
        vbox_right.addWidget(self.right_label_use)
        vbox_right.addWidget(self.right_label_find)
        vbox_right.addWidget(self.right_image_label)
        vbox_right.addStretch(1)

        hbox.addLayout(vbox_right, 7)

        # Set the main layout in the window
        self.setLayout(hbox)

        self.setWindowTitle('Minecraft Blocks Info')
        self.show()

    def button_clicked(self):
        sender = self.sender()
        text = sender.text()
        self.update_right_label(text)

    def update_right_label(self, text):
        block_info = {
            "Crafting Table": {
                "use": ("Crafting Table është një bllok që përdoret për të krijuar sende të ndryshme. "
                        "Kjo është baza për çdo bllok ose mjet në Minecraft dhe lejon lojtarët të krijojnë "
                        "çdo gjë nga vegla deri tek armaturat komplekse."),
                "find": ("Mund ta krijosh nga 4 Planks të çdo lloji druri. Vendosni Planks në një katror "
                         "2x2 në ekranin e crafting të inventarit tuaj."),
                "image": "craftingtable.png"
            },
            "Planks": {
                "use": ("Planks janë një material bazë për ndërtim, krijuar nga druri. "
                        "Ato përdoren për të ndërtuar struktura dhe krijuar sende të ndryshme si "
                        "Crafting Table, Chest dhe më shumë."),
                "find": "Mund të krijohen duke përpunuar drurin në Crafting Table.",
                "image": "planks.png"
            },
            "Stone": {
                "use": ("Stone është një material i zakonshëm që përdoret për ndërtim dhe krijimin e veglave. "
                        "Pasi të thyhet, ai kthehet në Cobblestone i cili mund të përdoret për të krijuar një "
                        "sërë sendesh."),
                "find": "Mund të gjendet duke shkatërruar blloqet e gurit me një vegël.",
                "image": "stone1.png",
            },
            "Furnace": {
                "use": ("Furnace përdoret për të shkrijë minerale dhe gatuar ushqim. "
                        "Është thelbësor për përpunimin e materialeve si Iron dhe Gold për të krijuar ingots."),
                "find": "Mund ta krijosh nga 8 blloqe Cobblestone në Crafting Table.",
                "image": "furnace.png"
            },
            "Chest": {
                "use": ("Chest është një bllok që përdoret për të ruajtur sende. "
                        "Mund të lidhni dy Chest për të krijuar një Double Chest me kapacitet më të madh."),
                "find": "Mund ta krijosh nga 8 Planks në Crafting Table.",
                "image": "chest.png"
            },
            "Torch": {
                "use": ("Torch është një bllok që siguron dritë dhe ndalon shfaqjen e monstrave. "
                        "Ato janë të dobishme për ndriçimin e minierave dhe strukturave."),
                "find": "Mund të krijohen nga një shkop dhe një thëngjill ose charcoal.",
                "image": "torch.png"
            },
            "Diamond": {
                "use": ("Diamond është një material i rrallë dhe i vlefshëm që përdoret për krijimin e veglave "
                        "dhe armaturave më të forta në lojë. Është gjithashtu i nevojshëm për tabelën e enchanments."),
                "find": ("Mund të gjendet në nivelet e ulëta të botës, zakonisht nga niveli 16 e poshtë. "
                         "Kërkoni për vein-eve të vogla në shpella dhe miniera."),
                "image": "diamond.png"
            },
            "Gold": {
                "use": ("Gold është një material që përdoret për krijimin e sendeve dekorative dhe të veçanta. "
                        "Gjithashtu përdoret për tregti dhe për krijimin e orëve dhe karrocave të minierës."),
                "find": "Mund të gjendet në nivelet e mesme të botës dhe në Nether.",
                "image": "gold.png"
                
            },
            "Iron": {
                "use": ("Iron është një material i fortë që përdoret për krijimin e veglave, armaturave dhe "
                        "strukturave. Është i domosdoshëm për shumë procese në lojë."),
                "find": "Mund të gjendet në nivelet e ndryshme të botës dhe të shkrihet në Furnace.",
                "image": "iron.png"
            },
            "Emerald": {
                "use": ("Emerald është një material që përdoret kryesisht për tregti me fshatarët. "
                        "Është mjaft i rrallë dhe ka një ngjyrë të gjelbër karakteristike."),
                "find": "Mund të gjendet në malet e larta dhe përmes tregtisë me fshatarët.",
                "image": "emerald.png"
            },
            "Redstone": {
                "use": ("Redstone është një material që përdoret për mekanizma dhe sinjalizime elektrike. "
                        "Është thelbësor për ndërtimin e makinave dhe strukturave të automatizuara."),
                "find": "Mund të gjendet në nivelet e ulëta të botës dhe në miniera.",
                "image": "redstone.png"
            },
            "Lapis Lazuli": {
                "use": ("Lapis Lazuli është një material që përdoret për zbukurime dhe enchanments. "
                        "Është i nevojshëm për të kryer enchanments në tabela të veçanta."),
                "find": "Mund të gjendet në nivelet e mesme të botës.",
                "image": "lapiz.png"
            },
            "Sand": {
                "use": ("Sand është një material që mund të shndërrohet në qelq. "
                        "Gjithashtu përdoret për krijimin e blloqeve të ndryshme si Sandstone."),
                "find": "Mund të gjendet në shkretëtira dhe afër ujit.",
                "image": "sand.png"
            },
            "Gravel": {
                "use": ("Gravel është një material që mund të japë Flint kur thyhet. "
                        "Është gjithashtu i dobishëm për krijimin e rrugëve."),
                "find": "Mund të gjendet në male, shpella dhe afër ujit.",
                "image": "gravel.png"
            },
            "Dirt": {
                "use": ("Dirt është një material bazë që gjendet kudo në botën e Minecraft-it. "
                        "Përdoret për të rritur bimët dhe për të ndërtuar terrene."),
                "find": "Mund të gjendet në sipërfaqe ose në thellësi të tokës.",
                "image": "dirt.png"
            },
            "Cobblestone": {
                "use": ("Cobblestone është një material që merret nga gurët dhe përdoret për ndërtim. "
                        "Është një nga materialet më të përdorura për krijimin e strukturave dhe veglave."),
                "find": "Mund të gjendet duke thyer Stone me një vegël.",
                "image": "coublestone.png"
            },
            "Wood": {
                "use": ("Wood është një material bazë që përdoret për shumë sende dhe struktura. "
                        "Mund të përpunohet në Planks për të krijuar më shumë sende."),
                "find": "Mund të gjendet nga pemët dhe të përpunohet në Planks.",
                "image": "wood.png"
            },
            "Grass Block": {
                "use": ("Grass Block është një bllok toke me bar mbi të. "
                        "Përdoret për të rritur barin dhe për dekorime."),
                "find": "Mund të gjendet në sipërfaqe ose të krijohet nga Dirt me Silk Touch.",
                "image": "grassblock.png"
            },
            "Glass": {
                "use": ("Glass është një material transparent që përdoret për dritare dhe dekorime. "
                        "Është shumë i dobishëm për ndërtimin e strukturave me ndriçim të mirë."),
                "find": "Mund të krijohet duke shkrirë Sand në Furnace.",
                "image": "glass.png"
            },
            "Brick": {
                "use": ("Brick është një material që përdoret për ndërtim dekorativ. "
                        "Është i fortë dhe i qëndrueshëm për ndërtimin e strukturave."),
                "find": "Mund të krijohet nga Clay Balls të shkrirë në Furnace.",
                "image": "brick.png"
            },
            "Obsidian": {
                "use": ("Obsidian është një material shumë i fortë që përdoret për portale dhe struktura të forta. "
                        "Është një nga materialet më të forta në lojë."),
                "find": "Mund të krijohet duke derdhur ujë mbi lavë dhe duke e thyer me një Diamond Pickaxe.",
                "image": "obsidian.png"
            },
            "Netherite": {
                "use": ("Netherite është materiali më i fortë që përdoret për vegla dhe armatura. "
                        "Është shumë më i fortë se Diamond dhe rezistent ndaj zjarrit."),
                "find": "Mund të krijohet duke kombinuar Ancient Debris me Gold Ingots.",
                "image": "netherite.png"
            },
            "Bedrock": {
                "use": ("Bedrock është një material i pathyeshëm që gjendet në fund të botës. "
                        "Përdoret për të kufizuar lojën dhe për të krijuar struktura të pathyeshme."),
                "find": "Mund të gjendet vetëm në fund të botës dhe nuk mund të thyhet.",
                "image": "badrock.png"
            },
            "Bucket of Water": {
                "use": ("Water është një lëng që përdoret për shumë qëllime në lojë. "
                        "Mund të përdoret për të krijuar ferma, për të transportuar sende dhe më shumë."),
                "find": "Mund të gjendet në liqene, lumenj dhe oqeane.",
                "image": "water.png"
            },
            "Bucket of Lava": {
                "use": ("Lava është një lëng që shkakton dëm dhe përdoret për shumë mekanizma. "
                        "Mund të përdoret për të krijuar Obsidian dhe për të eliminuar armiqtë."),
                "find": "Mund të gjendet në shpella dhe në Nether.",
                "image": "lava.png"
            },

            "Sword": {
                "use": ("Sword është një vegël për luftë që përdoret për të dëmtuar armiqtë. "
                        "Ka nivele të ndryshme të fuqisë, duke filluar nga Wood Sword deri tek Diamond Sword."),
                "find": "Mund të krijohet duke përdorur Planks dhe Sticks në Crafting Table.",
                "image": "sword.png"
            },
            "Bow": {
                "use": ("Bow është një armë që lëshon shigjeta për të dëmtuar armiqtë nga largësia. "
                        "Shigjetat duhet të mbushen me zvarrë në mënyrë që të jenë efektive."),
                "find": "Mund të krijohet duke përdorur String dhe Sticks në Crafting Table.",
                "image": "bow.png"
            },
            "Arrow": {
                "use": ("Arrow është një shigjetë që lëshohet nga Bow për të dëmtuar armiqtë. "
                        "Shigjetat janë të përshtatshme për të goditur armiqtë në distancë."),
                "find": "Mund të krijohet duke përdorur Feather, Stick, dhe flint në Crafting Table.",
                "image": "arrow.png"
            },
            "Shield": {
                "use": ("Shield është një mbrojtës që përdoret për të bllokuar sulmet e armiqve. "
                        "Mbron lojtarin nga dëmtimi dhe efektet e dëmeve si p.sh. flamujt."),
                "find": "Mund të krijohet duke përdorur Planks dhe Iron Ingots në Crafting Table.",
                "image": "shield.png"
            },
            "Iron Armor": {
                "use": ("Iron Armor eshte nje armor i perbere nga Iron i cili "
                        "ka nje mbrojtje mesatare."),
                "find": "Ai nuk mund te gjindet  por duhet te krijuar duke mbledhur iron nga toka.",
                "image": "ironarmor.png"
            },
            "Diamond Armor": {
                "use": ("Ky aror eshte nje nder armoret me te mire te lojes, ka nje mbrojtje te nivelit te larte."),
                "find": "Mund të krijohet duke përdorur vetem diamonds.",
                "image": "diamondarmor.png"
            },
            "Netherite Armor": {
                "use": ("Ky armor eshte armori me i fort qe ekziston ne loje, dhe ka mbrojtje te nivelit ekstreme."),
                "find": "Mund të krijohet duke përdorur vetem netherite.",
                "image": "netheritearmor.png"
            },
            "Enchanting Table": {
                "use": ("Enchanting Table eshte nje mjet i cili mundeson " 
                        "perforcimin e mjeteve luftuese dhe mbrojtese duke perdorur magjite"),
                "find": "Mund të krijohet duke përdorur diamonds, obsidian dhe books",
                "image": "enchantingtable.png"
            }
        }
        
        block = block_info.get(text, {"use": "Nuk ka përmbajtje për këtë bllok.", "find": "", "image": ""})
        self.right_label_use.setText(f"Përdorimi: {block['use']}")
        self.right_label_find.setText(f"Si ta gjesh: {block['find']}")

        if block['image']:
            pixmap = QPixmap(block['image'])
            if not pixmap.isNull():
                self.right_image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
            else:
                self.right_image_label.setText("Nuk mund të ngarkoj imazhin.")
        else:
            self.right_image_label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
