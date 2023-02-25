from enum import Enum

class CardTypes(Enum):
    """
    卡牌的种类。

    分为阵营牌，手牌，身份牌

    CAMP: 阵营牌
    HAND: 手牌
    PROFESSION: 身份牌
    """
    CAMP = 1 
    HAND = 2
    PROFESSION = 3


class Card(object):
    def __init__(
        self,
        id: int,
        card_type: CardTypes,
        description: str
    ) -> None:
        self.id:int = id
        self.card_type:CardTypes = card_type
        self.description = description
        self.name = self.description.split('，')[0]

class RedCamp(Card):
    '''
    id: 0

    红色阵营卡牌，当阵营中至少拥有三只高脚杯即可宣布胜利。
    '''
    def __init__(self) -> None:
        desc = '红色阵营卡牌，当阵营中至少拥有三只高脚杯即可宣布胜利。'
        super().__init__(0, CardTypes.CAMP, desc)
    def __str__(self):
        return str(self.id) + ' ' + self.description

class BlueCamp(Card):
    '''
    id: 1

    蓝色阵营卡牌，当阵营中至少拥有三把钥匙即可宣布胜利。
    '''
    def __init__(self) -> None:
        desc = '蓝色阵营卡牌，当阵营中至少拥有三把钥匙即可宣布胜利。'
        super().__init__(1, CardTypes.CAMP, desc)
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Goblet(Card):
    '''
    id: 2

    高脚杯，红色阵营拥有三张及以上即可宣布胜利。
    '''
    def __init__(self) -> None:
        desc = '高脚杯，红色阵营拥有三张及以上即可宣布胜利。'
        super().__init__(2, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Key(Card):
    '''
    id: 3

    钥匙，蓝色阵营拥有三张及以上即可宣布胜利。
    '''
    def __init__(self) -> None:
        desc = '钥匙，蓝色阵营拥有三张及以上即可宣布胜利。'
        super().__init__(3, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class GobletBag(Card):
    '''
    id: 4

    神秘手提袋，交易后可以从牌堆中摸一张牌，当牌堆耗尽后，变为一张高脚杯。
    '''
    def __init__(self) -> None:
        desc = '神秘手提袋，交易后可以从牌堆中摸一张牌，当牌堆耗尽后，变为一张高脚杯。'
        super().__init__(4, CardTypes.HAND, desc)
    def __str__(self):
        return str(self.id) + ' ' + self.description


class KeyBag(Card):
    '''
    id: 5

    神秘手提袋，交易后可以从牌堆中摸一张牌，当牌堆耗尽后，变为一张钥匙。
    '''
    def __init__(self) -> None:
        desc = '神秘手提袋，交易后可以从牌堆中摸一张牌，当牌堆耗尽后，变为一张钥匙。'
        super().__init__(5, CardTypes.HAND, desc)
    def __str__(self):
        return str(self.id) + ' ' + self.description
        

class Knife(Card):
    '''
    id: 6

    匕首，作为攻击者时，ATK+1，支援不适用
    '''
    def __init__(self) -> None:
        desc = '匕首，作为攻击者获得 ATK+1，支援不适用'
        super().__init__(6, CardTypes.HAND, desc)
    def __str__(self):
        return str(self.id) + ' ' + self.description
        

class Tome(Card):
    '''
    id: 7

    典籍，交换此物品，你可以与交易对象互换职业。
    '''
    def __init__(self) -> None:
        desc = '典籍，交换此物品，你可以与交易对象互换职业。'
        super().__init__(7, CardTypes.HAND, desc)
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Privileg(Card):
    '''
    id: 8

    特权状，交易此物品，你可以查看交易对象的手牌。
    '''
    def __init__(self) -> None:
        desc = '特权状，交易此物品，你可以查看交易对象的手牌。'
        super().__init__(8, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class PoisionRing(Card):
    '''
    id: 9

    毒戒指，你在不分胜负的战斗中获胜。
    '''
    def __init__(self) -> None:
        desc = '毒戒指，你在不分胜负的战斗中获胜。'
        super().__init__(9, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Gloves(Card):
    '''
    id: 10

    手套，作为防御者获得 DEF+1，支援不适用
    '''
    def __init__(self) -> None:
        desc = '手套，作为防御者获得 DEF+1，支援不适用'
        super().__init__(10, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Coat(Card):
    '''
    id: 11

    大衣，交易此物品，你可以重新选择一个未使用的职业。
    '''
    def __init__(self) -> None:
        desc = '大衣，交易此物品，你可以重新选择一个未使用的职业。'
        super().__init__(11, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Glass(Card):
    '''
    id: 12

    单片眼镜，交换此物品，查看对方的阵营。
    '''
    def __init__(self) -> None:
        desc = '单片眼镜，交换此物品，查看对方的阵营。'
        super().__init__(12, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Whip(Card):
    '''
    id: 13

    长鞭，支援防御方时使其获得 DEF+1
    '''
    def __init__(self) -> None:
        desc = '长鞭，支援防御方时使其获得 DEF+1'
        super().__init__(13, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class BlackPearl(Card):
    '''
    id: 14

    黑珍珠，在交易时必须接受，持有它的玩家不能宣告胜利。
    '''
    def __init__(self) -> None:
        desc = '黑珍珠，在交易时必须接受，持有它的玩家不能宣告胜利。'
        super().__init__(14, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Sextant(Card):
    '''
    id: 15

    六分仪，交易此物品，你可以指定一个方向，所有玩家必须将一个物品交给该方向的人，传递不视为交易。
    '''
    def __init__(self) -> None:
        desc = '六分仪，交易此物品，你可以指定一个方向，所有玩家必须将一个物品交给该方向的人，传递不视为交易。'
        super().__init__(15, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class RemoteKnife(Card):
    '''
    id: 16

    飞刀，支援进攻方时使其获得 ATK+1
    '''
    def __init__(self) -> None:
        desc = '飞刀，支援进攻方时使其获得 ATK+1'
        super().__init__(16, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class BrokenMirror(Card):
    '''
    id: 17

    破镜子，交易时不能拒绝，被交易者的物品效果不发动
    '''
    def __init__(self) -> None:
        desc = '破镜子，交易时不能拒绝，被交易者的物品效果不发动'
        super().__init__(17, CardTypes.HAND, desc)
        
    def __str__(self):
        return str(self.id) + ' ' + self.description

class Diplomat(Card):
    '''
    id: 18

    外交官，限用一次，指定某位玩家与你交易指定物品，如果对方没有该物品，那么可以查看对方手牌，并结束回合。
    '''
    def __init__(self) -> None:
        desc = '外交官，限用一次，指定某位玩家与你交易指定物品，如果对方没有该物品，那么可以查看对方手牌，并结束回合。'
        super().__init__(18, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Doctor(Card):
    '''
    id: 19

    医生，限用一次，发动后阻止战争的效果。
    '''
    def __init__(self) -> None:
        desc = '医生，限用一次，发动后阻止战争的效果。'
        super().__init__(19, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Duelist(Card):
    '''
    id: 20

    决斗者，限用一次，作为攻击者或防御者，你可以假定这场战争没有支援，并获得 ATK/DEF+1 。
    '''
    def __init__(self) -> None:
        desc = '决斗者，限用一次，作为攻击者或防御者，你可以假定这场战争没有支援，并获得 ATK/DEF+1 。'
        super().__init__(20, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Poisoner(Card):
    '''
    id: 21

    毒药师，限用一次，你可以指定战争的胜利者，但你不能是进攻/防守方。
    '''
    def __init__(self) -> None:
        desc = '毒药师，限用一次，你可以指定战争的胜利者，但你不能是进攻/防守方。'
        super().__init__(21, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class KungfuMaster(Card):
    '''
    id: 22

    武术宗师，作为防御者获得 DEF+1
    '''
    def __init__(self) -> None:
        desc = '武术宗师，作为防御者获得 DEF+1'
        super().__init__(22, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Xrayer(Card):
    '''
    id: 23

    透视者，限用一次，在你的回合，你可以查看牌堆并取出两件物品放在最上面
    '''
    def __init__(self) -> None:
        desc = '透视者，限用一次，在你的回合，你可以查看牌堆并取出两件物品放在最上面'
        super().__init__(23, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Hypnotist(Card):
    '''
    id: 24

    催眠师，如果你是攻击者，你可以指定某个玩家的支援无效。
    '''
    def __init__(self) -> None:
        desc = '催眠师，如果你是攻击者，你可以指定某个玩家的支援无效。'
        super().__init__(24, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Bodyguard(Card):
    '''
    id: 25

    保镖，你在战争中支持的玩家获得额外的ATK/DEF+1，对自身无效
    '''
    def __init__(self) -> None:
        desc = '保镖，你在战争中支持的玩家获得额外的ATK/DEF+1，对自身无效'
        super().__init__(25, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Godfather(Card):
    '''
    id: 26

    神父，在其他玩家宣布支援前阻止战争，如果攻击者至少有两张手牌，挑一张给你。
    '''
    def __init__(self) -> None:
        desc = '神父，在其他玩家宣布支援前阻止战争，如果攻击者至少有两张手牌，挑一张给你。'
        super().__init__(26, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

class Bully(Card):
    '''
    id: 27

    恶棍，作为攻击者获得 ATK+1，支援无效。
    '''
    def __init__(self) -> None:
        desc = '恶棍，作为攻击者获得 ATK+1，支援无效。'
        super().__init__(27, CardTypes.PROFESSION, desc)

    def __str__(self):
        return str(self.id) + ' ' + self.description

camp_cards = [RedCamp, BlueCamp]
hand_cards = [
    
]
