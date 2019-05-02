from PIL import Image, ImageTk

fuImage = ImageTk.PhotoImage(Image.open('images/fu.png'))
kyouImage = ImageTk.PhotoImage(Image.open('images/kyou.png'))
keImage = ImageTk.PhotoImage(Image.open('images/ke.png'))
ginImage = ImageTk.PhotoImage(Image.open('images/gin.png'))
kinImage = ImageTk.PhotoImage(Image.open('images/kin.png'))
ooImage = ImageTk.PhotoImage(Image.open('images/oo.png'))
gyouImage = ImageTk.PhotoImage(Image.open('images/gyou.png'))
hishaImage = ImageTk.PhotoImage(Image.open('images/hisha.png'))
kakuImage = ImageTk.PhotoImage(Image.open('images/kaku.png'))
toImage = ImageTk.PhotoImage(Image.open('images/to.png'))
narikyouImage = ImageTk.PhotoImage(Image.open('images/narikyou.png'))
narikeImage = ImageTk.PhotoImage(Image.open('images/narike.png'))
nariginImage = ImageTk.PhotoImage(Image.open('images/narigin.png'))
ryuuImage = ImageTk.PhotoImage(Image.open('images/ryuu.png'))
umaImage = ImageTk.PhotoImage(Image.open('images/uma.png'))

yellowfuImage = ImageTk.PhotoImage(Image.open('images/fu_yellow.png'))
yellowkyouImage = ImageTk.PhotoImage(Image.open('images/kyou_yellow.png'))
yellowkeImage = ImageTk.PhotoImage(Image.open('images/ke_yellow.png'))
yellowginImage = ImageTk.PhotoImage(Image.open('images/gin_yellow.png'))
yellowkinImage = ImageTk.PhotoImage(Image.open('images/kin_yellow.png'))
yellowooImage = ImageTk.PhotoImage(Image.open('images/oo_yellow.png'))
yellowgyouImage = ImageTk.PhotoImage(Image.open('images/gyou_yellow.png'))
yellowhishaImage = ImageTk.PhotoImage(Image.open('images/hisha_yellow.png'))
yellowkakuImage = ImageTk.PhotoImage(Image.open('images/kaku_yellow.png'))
yellowtoImage = ImageTk.PhotoImage(Image.open('images/to_yellow.png'))
yellownarikyouImage = ImageTk.PhotoImage(Image.open('images/narikyou_yellow.png'))
yellownarikeImage = ImageTk.PhotoImage(Image.open('images/narike_yellow.png'))
yellownariginImage = ImageTk.PhotoImage(Image.open('images/narigin_yellow.png'))
yellowryuuImage = ImageTk.PhotoImage(Image.open('images/ryuu_yellow.png'))
yellowumaImage = ImageTk.PhotoImage(Image.open('images/uma_yellow.png'))

vfuImage = ImageTk.PhotoImage(Image.open('images/v_fu.png'))
vkyouImage = ImageTk.PhotoImage(Image.open('images/v_kyou.png'))
vkeImage = ImageTk.PhotoImage(Image.open('images/v_ke.png'))
vginImage = ImageTk.PhotoImage(Image.open('images/v_gin.png'))
vkinImage = ImageTk.PhotoImage(Image.open('images/v_kin.png'))
vooImage = ImageTk.PhotoImage(Image.open('images/v_oo.png'))
vgyouImage = ImageTk.PhotoImage(Image.open('images/v_gyou.png'))
vhishaImage = ImageTk.PhotoImage(Image.open('images/v_hisha.png'))
vkakuImage = ImageTk.PhotoImage(Image.open('images/v_kaku.png'))
vtoImage = ImageTk.PhotoImage(Image.open('images/v_to.png'))
vnarikyouImage = ImageTk.PhotoImage(Image.open('images/v_narikyou.png'))
vnarikeImage = ImageTk.PhotoImage(Image.open('images/v_narike.png'))
vnariginImage = ImageTk.PhotoImage(Image.open('images/v_narigin.png'))
vryuuImage = ImageTk.PhotoImage(Image.open('images/v_ryuu.png'))
vumaImage = ImageTk.PhotoImage(Image.open('images/v_uma.png'))
zeroImage = ImageTk.PhotoImage(Image.open('images/zero.png'))

yellowvfuImage = ImageTk.PhotoImage(Image.open('images/v_fu_yellow.png'))
yellowvkyouImage = ImageTk.PhotoImage(Image.open('images/v_kyou_yellow.png'))
yellowvkeImage = ImageTk.PhotoImage(Image.open('images/v_ke_yellow.png'))
yellowvginImage = ImageTk.PhotoImage(Image.open('images/v_gin_yellow.png'))
yellowvkinImage = ImageTk.PhotoImage(Image.open('images/v_kin_yellow.png'))
yellowvooImage = ImageTk.PhotoImage(Image.open('images/v_oo_yellow.png'))
yellowvgyouImage = ImageTk.PhotoImage(Image.open('images/v_gyou_yellow.png'))
yellowvhishaImage = ImageTk.PhotoImage(Image.open('images/v_hisha_yellow.png'))
yellowvkakuImage = ImageTk.PhotoImage(Image.open('images/v_kaku_yellow.png'))
yellowvtoImage = ImageTk.PhotoImage(Image.open('images/v_to_yellow.png'))
yellowvnarikyouImage = ImageTk.PhotoImage(Image.open('images/v_narikyou_yellow.png'))
yellowvnarikeImage = ImageTk.PhotoImage(Image.open('images/v_narike_yellow.png'))
yellowvnariginImage = ImageTk.PhotoImage(Image.open('images/v_narigin_yellow.png'))
yellowvryuuImage = ImageTk.PhotoImage(Image.open('images/v_ryuu_yellow.png'))
yellowvumaImage = ImageTk.PhotoImage(Image.open('images/v_uma_yellow.png'))
yellowzeroImage = ImageTk.PhotoImage(Image.open('images/zero_yellow.png'))

gomaToImage_angleSente = {
	('先手', '步'):fuImage,
	('先手', '香'):kyouImage,
	('先手', '桂'):keImage,
	('先手', '銀'):ginImage,
	('先手', '金'):kinImage,
	('先手', '飛'):hishaImage,
	('先手', '角'):kakuImage,
	('先手', '王'):ooImage,
	('先手', 'と'):toImage,
	('先手', '杏'):narikyouImage,
	('先手', '圭'):narikeImage,
	('先手', '全'):nariginImage,
	('先手', '竜'):ryuuImage,
	('先手', '馬'):umaImage,
	('後手', '步'):vfuImage,
	('後手', '香'):vkyouImage,
	('後手', '桂'):vkeImage,
	('後手', '銀'):vginImage,
	('後手', '金'):vkinImage,
	('後手', '飛'):vhishaImage,
	('後手', '角'):vkakuImage,
	('後手', '王'):vgyouImage,
	('後手', 'と'):vtoImage,
	('後手', '杏'):vnarikyouImage,
	('後手', '圭'):vnarikeImage,
	('後手', '全'):vnariginImage,
	('後手', '竜'):vryuuImage,
	('後手', '馬'):vumaImage,
	('', '  '):zeroImage
}
gomaToImage_angleGote = {
	('後手', '步'):fuImage,
	('後手', '香'):kyouImage,
	('後手', '桂'):keImage,
	('後手', '銀'):ginImage,
	('後手', '金'):kinImage,
	('後手', '飛'):hishaImage,
	('後手', '角'):kakuImage,
	('後手', '王'):gyouImage,
	('後手', 'と'):toImage,
	('後手', '杏'):narikyouImage,
	('後手', '圭'):narikeImage,
	('後手', '全'):nariginImage,
	('後手', '竜'):ryuuImage,
	('後手', '馬'):umaImage,
	('先手', '步'):vfuImage,
	('先手', '香'):vkyouImage,
	('先手', '桂'):vkeImage,
	('先手', '銀'):vginImage,
	('先手', '金'):vkinImage,
	('先手', '飛'):vhishaImage,
	('先手', '角'):vkakuImage,
	('先手', '王'):vooImage,
	('先手', 'と'):vtoImage,
	('先手', '杏'):vnarikyouImage,
	('先手', '圭'):vnarikeImage,
	('先手', '全'):vnariginImage,
	('先手', '竜'):vryuuImage,
	('先手', '馬'):vumaImage,
	('', '  '):zeroImage
}

gomaToYellowImage_angleSente = {
	('先手', '步'):yellowfuImage,
	('先手', '香'):yellowkyouImage,
	('先手', '桂'):yellowkeImage,
	('先手', '銀'):yellowginImage,
	('先手', '金'):yellowkinImage,
	('先手', '飛'):yellowhishaImage,
	('先手', '角'):yellowkakuImage,
	('先手', '王'):yellowooImage,
	('先手', 'と'):yellowtoImage,
	('先手', '杏'):yellownarikyouImage,
	('先手', '圭'):yellownarikeImage,
	('先手', '全'):yellownariginImage,
	('先手', '竜'):yellowryuuImage,
	('先手', '馬'):yellowumaImage,
	('後手', '步'):yellowvfuImage,
	('後手', '香'):yellowvkyouImage,
	('後手', '桂'):yellowvkeImage,
	('後手', '銀'):yellowvginImage,
	('後手', '金'):yellowvkinImage,
	('後手', '飛'):yellowvhishaImage,
	('後手', '角'):yellowvkakuImage,
	('後手', '王'):yellowvgyouImage,
	('後手', 'と'):yellowvtoImage,
	('後手', '杏'):yellowvnarikyouImage,
	('後手', '圭'):yellowvnarikeImage,
	('後手', '全'):yellowvnariginImage,
	('後手', '竜'):yellowvryuuImage,
	('後手', '馬'):yellowvumaImage,
	('', '  '):yellowzeroImage
}
gomaToYellowImage_angleGote = {
	('後手', '步'):yellowfuImage,
	('後手', '香'):yellowkyouImage,
	('後手', '桂'):yellowkeImage,
	('後手', '銀'):yellowginImage,
	('後手', '金'):yellowkinImage,
	('後手', '飛'):yellowhishaImage,
	('後手', '角'):yellowkakuImage,
	('後手', '王'):yellowgyouImage,
	('後手', 'と'):yellowtoImage,
	('後手', '杏'):yellownarikyouImage,
	('後手', '圭'):yellownarikeImage,
	('後手', '全'):yellownariginImage,
	('後手', '竜'):yellowryuuImage,
	('後手', '馬'):yellowumaImage,
	('先手', '步'):yellowvfuImage,
	('先手', '香'):yellowvkyouImage,
	('先手', '桂'):yellowvkeImage,
	('先手', '銀'):yellowvginImage,
	('先手', '金'):yellowvkinImage,
	('先手', '飛'):yellowvhishaImage,
	('先手', '角'):yellowvkakuImage,
	('先手', '王'):yellowvooImage,
	('先手', 'と'):yellowvtoImage,
	('先手', '杏'):yellowvnarikyouImage,
	('先手', '圭'):yellowvnarikeImage,
	('先手', '全'):yellowvnariginImage,
	('先手', '竜'):yellowvryuuImage,
	('先手', '馬'):yellowvumaImage,
	('', '  '):yellowzeroImage
}