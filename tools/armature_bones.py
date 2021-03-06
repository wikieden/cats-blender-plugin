# MIT License

# Copyright (c) 2017 GiveMeAllYourCats

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Code author: Shotariya
# Repo: https://github.com/Grim-es/shotariya
# Code author: Neitri
# Repo: https://github.com/netri/blender_neitri_tools
# Edits by: GiveMeAllYourCats, Hotox

from collections import OrderedDict

bone_list = ['ControlNode', 'ParentNode', 'Center', 'CenterTip', 'Groove', 'Waist', 'EyesTip',
             'LowerBodyTip', 'UpperBody2Tip', 'GrooveTip', 'NeckTip']
bone_list_with = ['_Shadow_', '_Dummy_', 'Dummy_', 'WaistCancel', 'LegIKParent', 'LegIKTip', 'LegIK', 'ToeTipIK',
                  'ToeTipIKTip', 'ShoulderP_', 'EyeTip_', 'ThumbTip_', 'IndexFingerTip_', 'MiddleFingerTip_',
                  'RingFingerTip_', 'LittleFingerTip_', 'HandDummy_', 'HandTip_', 'ShoulderC_', 'SleeveShoulderIK_']
bone_list_parenting = {
    'Spine': 'Hips',
    'Chest': 'Spine',
    'Neck': 'Chest',
    'Head': 'Neck',
    'Left shoulder': 'Chest',
    'Right shoulder': 'Chest',
    'Left arm': 'Left shoulder',
    'Right arm': 'Right shoulder',
    'Left elbow': 'Left arm',
    'Right elbow': 'Right arm',
    'Left wrist': 'Left elbow',
    'Right wrist': 'Right elbow',
    'Left leg': 'Hips',
    'Right leg': 'Hips',
    'Left knee': 'Left leg',
    'Right knee': 'Right leg',
    'Left ankle': 'Left knee',
    'Right ankle': 'Right knee',
    'Left toe': 'Left ankle',
    'Right toe': 'Right ankle',

    'Thumb0_L': 'Left wrist',
    'IndexFinger1_L': 'Left wrist',
    'MiddleFinger1_L': 'Left wrist',
    'RingFinger1_L': 'Left wrist',
    'LittleFinger1_L': 'Left wrist',

    'Thumb1_L': 'Thumb0_L',
    'IndexFinger2_L': 'IndexFinger1_L',
    'MiddleFinger2_L': 'MiddleFinger1_L',
    'RingFinger2_L': 'RingFinger1_L',
    'LittleFinger2_L': 'LittleFinger1_L',

    'Thumb2_L': 'Thumb1_L',
    'IndexFinger3_L': 'IndexFinger2_L',
    'MiddleFinger3_L': 'MiddleFinger2_L',
    'RingFinger3_L': 'RingFinger2_L',
    'LittleFinger3_L': 'LittleFinger2_L',

    'Thumb0_R': 'Right wrist',
    'IndexFinger1_R': 'Right wrist',
    'MiddleFinger1_R': 'Right wrist',
    'RingFinger1_R': 'Right wrist',
    'LittleFinger1_R': 'Right wrist',

    'Thumb1_R': 'Thumb0_R',
    'IndexFinger2_R': 'IndexFinger1_R',
    'MiddleFinger2_R': 'MiddleFinger1_R',
    'RingFinger2_R': 'RingFinger1_R',
    'LittleFinger2_R': 'LittleFinger1_R',

    'Thumb2_R': 'Thumb1_R',
    'IndexFinger3_R': 'IndexFinger2_R',
    'MiddleFinger3_R': 'MiddleFinger2_R',
    'RingFinger3_R': 'RingFinger2_R',
    'LittleFinger3_R': 'LittleFinger2_R',

    # Special cases
    'M_head_copy': 'Head',
}
dont_delete_these_bones = {
    'Hips', 'Spine', 'Chest', 'Neck', 'Head',
    'Left leg', 'Left knee', 'Left ankle', 'Left toe',
    'Right leg', 'Right knee', 'Right ankle', 'Right toe',
    'Left shoulder', 'Left arm', 'Left elbow', 'Left wrist',
    'Right shoulder', 'Right arm', 'Right elbow', 'Right wrist',
    'OldRightEye', 'OldLeftEye', 'LeftEye', 'RightEye', 'Eye_L', 'Eye_R',

    'Thumb0_L', 'Thumb1_L', 'Thumb2_L',
    'IndexFinger1_L', 'IndexFinger2_L', 'IndexFinger3_L',
    'MiddleFinger1_L', 'MiddleFinger2_L', 'MiddleFinger3_L',
    'RingFinger1_L', 'RingFinger2_L', 'RingFinger3_L',
    'LittleFinger1_L', 'LittleFinger2_L', 'LittleFinger3_L',

    'Thumb0_R', 'Thumb1_R', 'Thumb2_R',
    'IndexFinger1_R', 'IndexFinger2_R', 'IndexFinger3_R',
    'MiddleFinger1_R', 'MiddleFinger2_R', 'MiddleFinger3_R',
    'RingFinger1_R', 'RingFinger2_R', 'RingFinger3_R',
    'LittleFinger1_R', 'LittleFinger2_R', 'LittleFinger3_R',

    'Breast_L', 'Breast_R',
}
bone_list_rename_unknown_side = {
    'Shoulder': 'shoulder',
    'Shoulder_001': 'shoulder'
}
bone_list_conflicting_names = [
    ('L_Clavicle', 'L_Shoulder', 'Arm_L'),
    ('R_Clavicle', 'R_Shoulder', 'Arm_R'),
    ('LeftCollar', 'LeftShoulder', 'Arm_L'),
    ('RightCollar', 'RightShoulder', 'Arm_R'),
    ('Left_Collar', 'Left Shoulder', 'Arm_L'),
    ('Right_Collar', 'Right Shoulder', 'Arm_R'),
    ('LeftUpLeg', 'LeftLeg', 'Knee_L'),
    ('RightUpLeg', 'RightLeg', 'Knee_R'),
]
bone_finger_list = [
    'Thumb0_',
    'IndexFinger1_',
    'MiddleFinger1_',
    'RingFinger1_',
    'LittleFinger1_',

    'Thumb1_',
    'IndexFinger2_',
    'MiddleFinger2_',
    'RingFinger2_',
    'LittleFinger2_',

    'Thumb2_',
    'IndexFinger3_',
    'MiddleFinger3_',
    'RingFinger3_',
    'LittleFinger3_',
]

################################
# Capitalize all bone names!
# Capitalize after each underscore!
# Replace '-' with '_'
# Replace ' ' with '_'
# Replace 'ValveBiped_' with ''
# Replace 'Bip01_' with 'Bip'
# Replace 'Bip001_' with 'Bip'
#
# Replace New Bone Patterns:
#   Left/Right = \Left
#   L/R = \L
# Replace Old Bone Patterns:
#   Left/Right = \Left
#   left/right = \left
#   L/R = \L
#   l/r = \l
################################
bone_rename = OrderedDict()
bone_rename['Hips'] = [
    'LowerBody',
    'Lowerbody',
    'Lower_Body',
    'Mixamorig:Hips',
    'Pelvis',
    'B_C_Pelvis',
    'B_C_Pelvis',
    'Bip_Pelvis',
    'Root',
    'Root_Hips',
    'Root_Rot',
    'Hip',
    'Sk',
]
bone_rename['Spine'] = [  # This is a list of all the spine and chest bones. They will be correctly fixed
    'Spine',  # First entry!

    # MMD
    'UpperBody',
    'Upperbody',
    'Upper_Body',
    'Upper_Waist',
    'UpperBody2',
    'Upperbody2',
    'Upper_Body_2',
    'Upper_Waist_2',
    'Waist_Upper_2',
    'UpperBody3',
    'Upperbody3',
    'Upper_Body_3',
    'Upper_Waist_3',
    'Waist_Upper_3',

    # Mixamo
    'Mixamorig:Spine',
    'Mixamorig:Spine0',
    'Mixamorig:Spine1',
    'Mixamorig:Spine2',
    'Mixamorig:Spine3',
    'Mixamorig:Spine4',

    # 3DMax?
    'Bip_Spine',
    'Bip_Spine0',
    'Bip_Spine1',
    'Bip_Spine2',
    'Bip_Spine3',
    'Bip_Spine4',
    'Bip_Spine5',
    'Bip_Spine_0',
    'Bip_Spine_1',
    'Bip_Spine_2',
    'Bip_Spine_3',
    'Bip_Spine_4',
    'Bip_Spine_5',
    'Bip_Chest',

    # Something
    'B_C_Spine',
    'B_C_Spine0',
    'B_C_Spine1',
    'B_C_Spine2',
    'B_C_Spine3',
    'B_C_Spine4',
    'B_C_Spine5',
    'B_C_Chest',

    # .Mesh
    'Spine_Lower',
    'Spine_Upper',

    'Abdomen',

    'Spine0',
    'Spine1',
    'Spine2',
    'Spine3',
    'Spine4',
    'Spine5',

    'Spine_0',
    'Spine_1',
    'Spine_2',
    'Spine_3',
    'Spine_4',
    'Spine_5',

    'Spine_01',
    'Spine_02',
    'Spine_03',
    'Spine_04',
    'Spine_05',

    'Chest1',
    'Chest2',
    'Chest3',

    'Chest_A',
    'Chest_B',
    'Chest_C',
    'Chest_D',
    'Chest_E',

    'Chest'  # Last entry!
]
bone_rename['Neck'] = [
    'Mixamorig:Neck',
    'Head_Neck_Lower',
    'Bip_Neck',
    'Bip_Neck1',
    'B_C_Neck1',
    'B_C_Neck1',
]
bone_rename['Head'] = [
    'Mixamorig:Head',
    'Head_Neck_Upper',
    'Bip_Head',
    'Bip_Head1',
    'B_C_Head',
    'B_C_Head',
]
bone_rename['\Left shoulder'] = [
    '\Left_Shoulder',
    '\LeftShoulder',
    'Shoulder_\L',
    '\LShoulder',
    '\L_Shoulder',
    'Mixamorig:\LeftShoulder',
    'Arm_\Left_Shoulder_1',
    'ShoulderArm_\L',
    'Bip_\L_Clavicle',
    'Bip_Collar_\L',
    'B_\L_Shoulder',
    'B_\L_Shoulder',
    'Shoulder_\L',
    '\LCollar',
    '\L_Clavicle',
    '\Left_Clavicle',
    '\Left_Clavicle',
    '\LeftCollar',
    '\Left_Collar',
    '\L_Collar',
]
bone_rename['\Left arm'] = [
    '\Left_Arm',
    '\LeftArm',
    'Arm_\L',
    '\LArm',
    '\LArmA',
    'ArmTC_\L',
    '+_\Left_Elbow_Support',
    '+_\Left_Elbow_Support',
    'Mixamorig:\LeftArm',
    'Arm_\Left_Shoulder_2',
    'Bip_\L_UpperArm',
    'Bip_UpperArm_\L',
    'B_\L_Arm1',
    'B_\L_Arm1',
    'Upper_Arm_\L',
    '\Left_Upper_Arm',
    '\LShldr',
    'Upper_Arm_\L',
    '\L_Upperarm',
    '\LeftUpArm',
    'Uparm_\L',
    '\L_Uparm',
    '\L_Arm',
    '\L_Arm_01',
]
bone_rename['Left arm'] = [
    '+_Leisure_Elder_Supplement',
]
bone_rename['\Left elbow'] = [
    '\Left_Elbow',
    '\LeftElbow',
    'Elbow_\L',
    '\L_Elbow',
    'Mixamorig:\LeftForeArm',
    'Arm_\Left_Elbow',
    'Bip_\L_Forearm',
    'Bip_LowerArm_\L',
    'B_\L_Arm2',
    'B_\L_Arm2',
    'Forearm_\L',
    '\LForeArm',
    'Forearm_\L',
    '\L_Forearm',
    '\LeftLowArm',
    '\Left_Forearm',
    '\L_Foarm',
    'Loarm_\L',
    '\L_Arm_02',
    '\LeftForeArm',
]
bone_rename['\Left wrist'] = [
    '\Left_Wrist',
    '\LeftWrist',
    'Wrist_\L',
    'Wrist2_\L',
    'HandAux2_\L',
    'Mixamorig:\LeftHand',
    'Arm_\Left_Wrist',
    'Bip_\L_Hand',
    'Bip_Hand_\L',
    'B_\L_Hand',
    'B_\L_Hand',
    'Hand_\L',
    '\LHand',
    'Hand_\L',
    '\L_Hand',
    '\LeftHand',
    '\Left_Hand',
    'Finger3_1_\L',
]
bone_rename['\Left leg'] = [
    '\Left_Leg',
    '\Left_foot',
    '\LeftLeg',
    'Leg_\L_001',
    'Leg_\L',
    'LegWAux_\L',
    'Leg00003333_\L',
    'Leg00004444_\L',
    'Mixamorig:\LeftUpLeg',
    'Leg_\Left_Thigh',
    'Bip_\L_Thigh',
    'Bip_Hip_\L',
    'B_\L_Leg1',
    'B_\L_Leg1',
    'Upper_Leg_\L',
    '\LThigh',
    'Thigh_\L',
    '\L_Thigh',
    '\LeftUpLeg',
    '\LeftHip',
    '\Left_Thigh',
    'Upleg_\L',
    '\L_Hip',
    '\L_Leg_01',
    '\L_Femur',
    'Waist_Cancel_\Left',
    'Waist_Cancellation_\Left',
]
bone_rename['\Left knee'] = [
    '\Left_Knee',
    '\LeftKnee',
    'Knee_\L_001',
    'Knee_\L',
    'Mixamorig:\LeftLeg',
    'Leg_\Left_Knee',
    'Bip_\L_Calf',
    'Bip_Knee_\L',
    'B_\L_Leg2',
    'B_\L_Leg2',
    'Lower_Leg_\L',
    '\LLeg',
    '\LShin',
    'Shin_\L',
    '\L_Calf',
    '\LeftLowLeg',
    '\Left_Shin',
    'Loleg_\L',
    '\L_Leg_02',
    '\L_KneeLower',
    'Tibia_\L',
    '\L_Tibia',
]
bone_rename['\Left ankle'] = [
    '\Left_Ankle',
    '\Left_Ankle_001',
    '\LeftAnkle',
    'Ankle_\L',
    'Mixamorig:\LeftFoot',
    'Leg_\Left_Ankle',
    'Bip_\L_Foot',
    'Bip_Foot_\L',
    'B_\L_Foot',
    'B_\L_Foot',
    'Lower',
    '\LFoot',
    'Foot_\L',
    '\L_Foot',
    '\LeftFoot',
    '\Left_Foot',
    'Leg_\Left_Foot',
    '\L_Foot_01',
    'LegIK_\L',
]
bone_rename['\Left toe'] = [
    '\Left_Toe',
    '\LeftToe',
    'LegTip_\L',
    'LegTipEX_\L',
    'ClawTipEX_\L',
    'Mixamorig:\LeftToeBase',
    'Leg_\Left_Toes',
    'Bip_\L_Toe0',
    'B_\L_Toe',
    'B_\L_Toe',
    '\LToe',
    'Toe_\L',
    '\L_Toe',
    '\LeftToeBase',
    'Toe1_1_\L',
    'Leg_\Left_Foot_Toes',
    'ToeSaki_\L',
    '\L_Toes',
]
bone_rename['Eye_\L'] = [
    '\Left_Eye',
    'Mixamorig:\LeftEye',
    'Head_Eyeball_\Left',
    'FEye\L',
    'Eye\L',
    '\L_Eye',
    'Bip_Eyeball_\L',
    '\L_EYE',
    'G_Eye_\L',
]
bone_rename['Eye_L'] = [
    'Eyes',
]
bone_rename['Eye_R'] = [
    'HL',
]

################################
# Capitalize all bone names!
# Capitalize after each underscore!
# Replace '-' with '_'
# Replace ' ' with '_'
# Replace 'ValveBiped_' with ''
# Replace 'Bip01_' with 'Bip'
# Replace 'Bip001_' with 'Bip'
#
# Replace New Bone Patterns:
#   Left/Right = \Left
#   L/R = \L
# Replace Old Bone Patterns:
#   Left/Right = \Left
#   left/right = \left
#   L/R = \L
#   l/r = \l
################################
bone_reweight = OrderedDict()
bone_reweight['Hips'] = [
    'LowerBody1',
    'Lowerbody2',
    'Pelvis_Adj',
    'Waist',
]
bone_reweight['Spine'] = [
    'UpperBodyx',
    'Spine_Lower_Adj',
    'Spine_Middle_Adj',
    'Bip_Spine0a',
]
bone_reweight['Chest'] = [
    'UpperBodyx2',
    'Spine_Upper_Adj',
    'Bip_Spine1a',
]
bone_reweight['Neck'] = [
    'Neckx',
    'NeckW',
    'NeckW2',
]
bone_reweight['Head'] = [
    'Neckx2',
]
bone_reweight['\Left shoulder'] = [
    'ShoulderC_\L',
    'ShoulderP_\L',
    'Shoulder2_\L',
    'ShoulderSleeve_\L',
    'SleeveShoulderIK_\L',
    '\Left_Shoulder_Weight',
    'ShoulderS_\L',
    'ShoulderW_\L',
    'Arm_\Left_Shoulder_Adj_1',
    'B_\L_ArmorParts',
    'Bip_\L_Shoulder',
    'Kata_\L',
]
bone_reweight['\Left arm'] = [
    'Arm01_\L',
    'Arm02_\L',
    'Arm03_\L',
    'Arm04_\L',
    'Arm05_\L',
    'ArmTwist_\L',
    'ArmTwist0_\L',
    'ArmTwist1_\L',
    'ArmTwist2_\L',
    'ArmTwist3_\L',
    'ArmTwist4_\L',
    '\Left_Arm_Twist',
    '\Left_Arm_Torsion',
    '\Left_Arm_Torsion_1',
    '\Left_Arm_Tight',
    '\Left_Arm_Tight_1',
    '\Left_Arm_Tight_2',
    '\Left_Arm_Tight_3',
    '\Left_Upper_Arm_Twist',
    '\Left_Upper_Arm_Twist_B',
    'ElbowAux_\L',
    'ElbowAux+_\L',
    '+ElbowAux_\L',
    'ArmSleeve_\L',
    'Arm_Sleeve_\L',
    'ArmTwist_Sleeve_\L',
    'ShoulderTwist_\L',
    'ArmW_\L',
    'ArmW2_\L',
    # 'Sleeve1_\L',
    'SleeveArm_\L',
    'SleeveElbowAux_\L',
    'ArmxcIa_\L',
    'ArmRotation_\L',
    'ArmTwistReturn_\L',
    'DEF_Upper_Arm_02_\L',
    'DEF_Upper_Arm_Twist_25_\L',
    'DEF_Upper_Arm_Twist_50_\L',
    'DEF_Upper_Arm_Twist_75_\L',
    'Arm_\Left_Shoulder_Adj_2',
    'Arm_\Left_Shoulder_Adj_3',
    'Arm_\Left_Shoulder_Adj_4',
    'Arm_\Left_Bicep',
    '\LArmB',
    '\L_Sub_Shoulder',
    'X_\L_ArmZoom1',
    'X_\L_ArmZoom2',
    'X_\L_ArmZoom3',
    'X_\L_ArmZoom4',
    'X_\L_ArmZoom5',
    'B_\L_Elbow',
    'B_\L_ArmHelper',
    'B_\L_UpperArm_Hojo01',
    'B_\L_Hiji01',
    'Bip_\L_Shoulder',
    'Bip_\L_Trapezius',
    'Bip_\L_Bicep',
    'Arm_\Left_Elbow_Ctr',
    'Arm_\Left_Shoulder_Ctr_1',
    '\L_Sho_Ast',
    '\L_Arm_Ast',
    'Uppertwist1_\L',
]
bone_reweight['Left arm'] = [  # This has apparently no side in the name
    'エプロンArm',
]
bone_reweight['\Left elbow'] = [
    'Elbow1_\L',
    'Elbow2_\L',
    'Elbow3_\L',
    'Elbow01_\L',
    'Elbow02_\L',
    'Elbow03_\L',
    'Elbow04_\L',
    'Elbow05_\L',
    'HandTwist_\L',
    'HandTwist1_\L',
    'HandTwist2_\L',
    'HandTwist3_\L',
    'HandTwist4_\L',
    '\Left_Hand_1',
    '\Left_Hand_2',
    '\Left_Hand_3',
    '\Left_Hand_Twist',
    '\Left_Hand_Twist_1',
    '\Left_Hand_Twist_2',
    '\Left_Hand_Thread_3',
    'ElbowSleeve_\L',
    'WristAux_\L',
    'ElbowTwist_\L',
    'ElbowTwist2_\L',
    'ElbowW_\L',
    'ElbowW2_\L',
    # 'Sleeve2_\L',
    'SleeveElbow_\L',
    'Elbow_Sleeve_\L',
    'SleeveMouth_\L',
    'ElbowRotation_\L',
    'HandTwistRotation1_\L',
    'HandTwistRotation2_\L',
    'DEF_Upper_Arm_Elbow_\L',
    'DEF_Forearm_Twist_25_\L',
    'DEF_Forearm_Twist_50_\L',
    'DEF_Forearm_Twist_75_\L',
    '+Elbow_\L',
    'Elbowa_\L',
    'Arm_\Left_Wrist_Adj',
    'Arm_\Left_Elbow_Adj_2',
    'Arm_\Left_Elbow_Adj_1',
    'Arm_\Left_Forearm'
    '\Left_Forearm_Twist'
    '\LHandEX',
    '\L_Sub_Elbow',
    'X_\L_ArmZoom6',
    'X_\L_ArmZoom7',
    'X_\L_ArmZoom8',
    'X_\L_ArmZoom9',
    'X_\L_ArmZoom10',
    'B_\L_ArmRoll',
    'Bip_\L_ForeTwist',
    'Bip_\L_ForeTwist1',
    'Bip_\L_Elbow',
    'Bip_\L_Ulna',
    'Bip_\L_Wrist',
    'Arm_\Left_Wrist_Ctr',
    '\L_Elb_Ast',
    '\L_Wrist_Ast',
    'Foretwist_\L',
    'Foretwist1_\L',
]
bone_reweight['\Left wrist'] = [
    # 'Sleeve3_\L',
    'WristSleeve_\L',
    'WristW_\L',
    'WristS_\L',
    'HandTwist5_\L',
    'IndexFinger0_\L',
    'MiddleFinger0_\L',
    'RingFinger0_\L',
    'LittleFinger0_\L',
    'DEF_Hand_\L',
    'DEF_Halm_01_\L',
    'DEF_Halm_02_\L',
    'DEF_Halm_03_\L',
    'DEF_Halm_04_\L',
    'Arm_\Left_Hand',
]
bone_reweight['\Left leg'] = [
    'LegD_\L',
    '+LegD_\L',
    '\Left_Foot_D',
    '\Left_Foot_Complement',
    '\Left_Foot_Supplement',
    'LegcntEven_\L',
    '\LLegTwist1',
    '\LLegTwist2',
    '\LLegTwist3',
    '\Left_Leg_Twist',
    'LegW_\L',
    'LegW2_\L',
    'LowerKnee_\L',
    'UpperKnee_\L',
    'LegX1_\L',
    'LegX2_\L',
    'LegX3_\L',
    '\Left_Knee_EX',
    '\Left_Foot_EX',
    'KneeEX_\L',
    'LegEX_\L',
    'Thigh_\L',
    'Leg+_\L',
    'Leg++_\L',
    'Leg+++_\L',
    'Leg++++_\L',
    'Knee++_\L',
    'Peaches_\L',
    'Pants_Stuff_000_\L',
    'Pants_Stuff_001_\L',
    'DEF_Thigh_Sub_\L',
    'DEF_Thigh_01_\L',
    'DEF_Thigh_02_\L',
    'DEF_Thigh_Twist_25_\L',
    'DEF_Thigh_Twist_50_\L',
    'DEF_Thigh_Twist_75_\L',
    'Leg_\Left_Thigh_Adj_1',
    'Leg_\Left_Thigh_Adj_2',
    'Leg_\Left_Thigh_Adj_3',
    'B_\L_LegHelper',
    'B_\L_Knee',
    'Leg_\Left_Thigh_Ctr',
    'Leg_\Left_Knee_Ctr',
    'B_\L_Hiza01',
    'B_\L_Pelvis_Hojo01',
    'Bip_\L_ThighTwist',
    'Bip_\L_ThighTwist1',
    '\L_KneeUpper',
    '\L_Tro_Ast',
    'Momotwist_\L',
    'Momotwist2_\L',
    'Momoniku_\L',
    '+_\Left_Foot_D',
]
bone_reweight['\Left knee'] = [
    'KneeD_\L',
    '\Left_Knee_D',
    'KneecntEven_\L',
    '\LTibiaTwist1',
    '\LTibiaTwist2',
    '\LTibiaTwist3',
    'KneeW1_\L',
    'KneeW2_\L',
    'Knee+_\L',
    'Knee+++_\L',
    'Knee++++_\L',
    'Ankle++_\L',
    'KneeArmor2_\L',
    'KneeX1_\L',
    'KneeX2_\L',
    'KneeX3_\L',
    'Leg_\Left_Acc',
    '\Left_Knee_Twist',
    '\Left_Ankle_EX',
    'AnkleEX_\L',
    'KneeAux_\L',
    'Shin_\L',
    'DEF_Knee_\L',
    'DEF_Knee_02_\L',
    'DEF_Shin_01_\L',
    'DEF_Shin_02_\L',
    'DEF_Shin_Twist_25_\L',
    'DEF_Shin_Twist_50_\L',
    'DEF_Shin_Twist_75_\L',
    'Leg_\Left_Ankle_Adj',
    'Leg_\Left_Knee_Adj_1',
    'Leg_\Left_Knee_Adj_2',
    '\L_Knee_Ast',
]
bone_reweight['\Left ankle'] = [
    'AnkleD_\L',
    '\Left_Ankle_D',
    'AnkleEven_\L',
    'AnkleW1_\L',
    'AnkleW2_\L',
    'ToeTipMovable_\L',
    'AnkleArmor_\L',
    'LowerUseless_\L',
    'Ankle+_\L',
    'Ankle+++_\L',
    'Ankle++++_\L',
    'DEF_Foot_\L',
    'LegA_L',
]
bone_reweight['\Left toe'] = [
    '\Left_Toes',
    'ClawTipEX_\L',
    'ClawTipEX2_\L',
    'ClawTipThumbEX_\L',
    'ClawTipThumbEX2_\L',
    '\Left_Toe_EX',
    '\Left_Foot_Tip_EX',
    'LegTip2_\L',
    'DEF_Toe_\L',
    'Bip_\L_Toe01',
    'Bip_\L_Toe1',
    'Bip_\L_Toe11',
    'Bip_\L_Toe2',
    'Bip_\L_Toe21',
]
bone_reweight['Eye_\L'] = [
    'EyeW_\L',
    'EyeLight_\L',
    'EyeLight1_\L',
    'EyeLight2_\L',
    'EyeLight3_\L',
    'EyeLight4_\L',
    'EyeReturn_\L',
    '\Left_Eye_Return',
    'Pupil_\L',
    '\Left_Pupil',
    '\Left_Eye_Glint',
    'Highlight_\L',
    'F_EyeTip_\L',
    'F_EyeLight1_\L',
    'F_EyeLight2_\L',
    'F_EyeLight3_\L',
    'DEF_Eye_\L',
    'EyeLight+_\L',
    'EyeRotationErase_\L',
]
bone_reweight['Breast_\L'] = [
    'DEF_Bust_01_\L',
    'DEF_Bust_02_\L',
]

# Secondary reweight list.
bone_list_weight = {
    # Other model fixes
    'DEF_Zipper': 'Zipper',
    'B F Mune01': 'Breasts',

    # Finger fixing
    # Left
    'DEF_Thumb_01_L_01': 'Thumb0_L',
    'DEF_Thumb_01_L_02': 'Thumb0_L',
    'DEF_Thumb_02_L': 'Thumb1_L',
    'DEF_Thumb_03_L': 'Thumb2_L',

    'DEF_F_Index_01_L_01': 'IndexFinger1_L',
    'DEF_F_Index_01_L_02': 'IndexFinger1_L',
    'DEF_F_Index_02_L': 'IndexFinger2_L',
    'DEF_F_Index_03_L': 'IndexFinger3_L',

    'DEF_F_Middle_01_L_01': 'MiddleFinger1_L',
    'DEF_F_Middle_01_L_02': 'MiddleFinger1_L',
    'DEF_F_Middle_02_L': 'MiddleFinger2_L',
    'DEF_F_Middle_03_L': 'MiddleFinger3_L',

    'DEF_F_Ring_01_L_01': 'RingFinger1_L',
    'DEF_F_Ring_01_L_02': 'RingFinger1_L',
    'DEF_F_Ring_02_L': 'RingFinger2_L',
    'DEF_F_Ring_03_L': 'RingFinger3_L',

    'DEF_F_Pinky_01_L_01': 'LittleFinger1_L',
    'DEF_F_Pinky_01_L_02': 'LittleFinger1_L',
    'DEF_F_Pinky_02_L': 'LittleFinger2_L',
    'DEF_F_Pinky_03_L': 'LittleFinger3_L',

    # Right
    'DEF_Thumb_01_R_01': 'Thumb0_R',
    'DEF_Thumb_01_R_02': 'Thumb0_R',
    'DEF_Thumb_02_R': 'Thumb1_R',
    'DEF_Thumb_03_R': 'Thumb2_R',

    'DEF_F_Index_01_R_01': 'IndexFinger1_R',
    'DEF_F_Index_01_R_02': 'IndexFinger1_R',
    'DEF_F_Index_02_R': 'IndexFinger2_R',
    'DEF_F_Index_03_R': 'IndexFinger3_R',

    'DEF_F_Middle_01_R_01': 'MiddleFinger1_R',
    'DEF_F_Middle_01_R_02': 'MiddleFinger1_R',
    'DEF_F_Middle_02_R': 'MiddleFinger2_R',
    'DEF_F_Middle_03_R': 'MiddleFinger3_R',

    'DEF_F_Ring_01_R_01': 'RingFinger1_R',
    'DEF_F_Ring_01_R_02': 'RingFinger1_R',
    'DEF_F_Ring_02_R': 'RingFinger2_R',
    'DEF_F_Ring_03_R': 'RingFinger3_R',

    'DEF_F_Pinky_01_R_01': 'LittleFinger1_R',
    'DEF_F_Pinky_01_R_02': 'LittleFinger1_R',
    'DEF_F_Pinky_02_R': 'LittleFinger2_R',
    'DEF_F_Pinky_03_R': 'LittleFinger3_R',
}

bone_rename_fingers = OrderedDict()
bone_rename_fingers['Thumb0_\L'] = [
    'Arm_\Left_Finger_1a',
    '\LThumb1',
    'Thumb_01_\L',
    '\L_Thumb0',
    '\L_Thumb_01',
    '\LeftHandThumb1',
    '\LeftFinger0',
    'Finger1_2_\L',
    'H_\L_Thumb1',
    'Bip_Thumb_0_\L',
    'Bip_\L_Finger0',
    '\L_Fing1_A',
]
bone_rename_fingers['Thumb1_\L'] = [
    'Arm_\Left_Finger_1b',
    '\LThumb2',
    'Thumb_02_\L',
    '\L_Thumb1',
    '\L_Thumb_02',
    '\LeftHandThumb2',
    '\LeftFinger01',
    'Finger1_3_\L',
    'H_\L_Thumb2',
    'Bip_Thumb_1_\L',
    'Bip_\L_Finger01',
    '\L_Fing1_B',
]
bone_rename_fingers['Thumb2_\L'] = [
    'Arm_\Left_Finger_1c',
    '\LThumb3',
    'Thumb_03_\L',
    '\L_Thumb2',
    '\L_Thumb_03',
    '\LeftHandThumb3',
    '\LeftFinger02',
    'Finger1_4_\L',
    'H_\L_Thumb3',
    'Bip_Thumb_2_\L',
    'Bip_\L_Finger02',
    '\L_Fing1_C',
]
bone_rename_fingers['IndexFinger1_\L'] = [
    'Fore1_\L',
    'Arm_\Left_Finger_2a',
    '\LIndex1',
    'F_Index_01_\L',
    '\L_Index0',
    '\L_Index_01',
    '\LeftHandIndex1',
    '\LeftFinger1',
    'Finger2_2_\L',
    'H_\L_Index1',
    'Bip_Index_0_\L',
    'Bip_\L_Finger1',
    '\L_Fing2_A',
]
bone_rename_fingers['IndexFinger2_\L'] = [
    'Fore2_\L',
    'Arm_\Left_Finger_2b',
    '\LIndex2',
    'F_Index_02_\L',
    '\L_Index1',
    '\L_Index_02',
    '\LeftHandIndex2',
    '\LeftFinger11',
    'Finger2_3_\L',
    'H_\L_Index2',
    'Bip_Index_1_\L',
    'Bip_\L_Finger11',
    '\L_Fing2_B',
]
bone_rename_fingers['IndexFinger3_\L'] = [
    'Fore3_\L',
    'Arm_\Left_Finger_2c',
    '\LIndex3',
    'F_Index_03_\L',
    '\L_Index2',
    '\L_Index_03',
    '\LeftHandIndex3',
    '\LeftFinger12',
    'Finger2_4_\L',
    'H_\L_Index3',
    'Bip_Index_2_\L',
    'Bip_\L_Finger12',
    '\L_Fing2_C',
]
bone_rename_fingers['MiddleFinger1_\L'] = [
    'Middle1_\L',
    'Arm_\Left_Finger_3a',
    '\LMid1',
    'F_Middle_01_\L',
    '\L_Mid0',
    '\L_Middle_01',
    '\L_Middle1',
    '\LeftHandMiddle1',
    '\LeftFinger2',
    'Finger3_2_\L',
    'H_\L_Middle1',
    'Bip_Middle_0_\L',
    'Bip_\L_Finger2',
    '\L_Fing3_A',
]
bone_rename_fingers['MiddleFinger2_\L'] = [
    'Middle2_\L',
    'Arm_\Left_Finger_3b',
    '\LMid2',
    'F_Middle_02_\L',
    '\L_Mid1',
    '\L_Middle_02',
    '\L_Middle2',
    '\LeftHandMiddle2',
    '\LeftFinger21',
    'Finger3_3_\L',
    'H_\L_Middle2',
    'Bip_Middle_1_\L',
    'Bip_\L_Finger21',
    '\L_Fing3_B',
]
bone_rename_fingers['MiddleFinger3_\L'] = [
    'Middle3_\L',
    'Arm_\Left_Finger_3c',
    '\LMid3',
    'F_Middle_03_\L',
    '\L_Mid2',
    '\L_Middle_03',
    '\LeftHandMiddle3',
    '\LeftFinger22',
    'Finger3_4_\L',
    'H_\L_Middle3',
    'Bip_Middle_2_\L',
    'Bip_\L_Finger22',
    '\L_Fing3_C',
]
bone_rename_fingers['RingFinger1_\L'] = [
    'Third1_\L',
    'Arm_\Left_Finger_4a',
    '\LRing1',
    'F_Ring_01_\L',
    '\L_Ring0',
    '\L_Ring_01',
    '\LeftHandRing1',
    '\LeftFinger3',
    'Finger4_2_\L',
    'H_\L_Ring1',
    'Bip_Ring_0_\L',
    'Bip_\L_Finger3',
    '\L_Fing4_A',
]
bone_rename_fingers['RingFinger2_\L'] = [
    'Third2_\L',
    'Arm_\Left_Finger_4b',
    '\LRing2',
    'F_Ring_02_\L',
    '\L_Ring1',
    '\L_Ring_02',
    '\LeftHandRing2',
    '\LeftFinger31',
    'Finger4_3_\L',
    'H_\L_Ring2',
    'Bip_Ring_1_\L',
    'Bip_\L_Finger31',
    '\L_Fing4_B',
]
bone_rename_fingers['RingFinger3_\L'] = [
    'Third3_\L',
    'Arm_\Left_Finger_4c',
    '\LRing3',
    'F_Ring_03_\L',
    '\L_Ring2',
    '\L_Ring_03',
    '\LeftHandRing3',
    '\LeftFinger32',
    'Finger4_4_\L',
    'H_\L_Ring3',
    'Bip_Ring_2_\L',
    'Bip_\L_Finger32',
    '\L_Fing4_C',
]
bone_rename_fingers['LittleFinger1_\L'] = [
    'Little1_\L',
    'Arm_\Left_Finger_5a',
    '\LPinky1',
    'F_Pinky_01_\L',
    '\L_Pinky0',
    '\L_Pinkey_01',
    '\LeftHandPinky1',
    '\LeftFinger4',
    'Finger5_2_\L',
    'H_\L_Pinky1',
    'Bip_Pinky_0_\L',
    'Bip_\L_Finger4',
    '\L_Fing5_A',
]
bone_rename_fingers['LittleFinger2_\L'] = [
    'Little2_\L',
    'Arm_\Left_Finger_5b',
    '\LPinky2',
    'F_Pinky_02_\L',
    '\L_Pinky1',
    '\L_Pinkey_02',
    '\LeftHandPinky2',
    '\LeftFinger41',
    'Finger5_3_\L',
    'H_\L_Pinky2',
    'Bip_Pinky_1_\L',
    'Bip_\L_Finger41',
    '\L_Fing5_B',
]
bone_rename_fingers['LittleFinger3_\L'] = [
    'Little3_\L',
    'Arm_\Left_Finger_5c',
    '\LPinky3',
    'F_Pinky_03_\L',
    '\L_Pinky2',
    '\L_Pinkey_03',
    '\LeftHandPinky3',
    '\LeftFinger42',
    'Finger5_4_\L',
    'H_\L_Pinky3',
    'Bip_Pinky_2_\L',
    'Bip_\L_Finger42',
    '\L_Fing5_C',
]
