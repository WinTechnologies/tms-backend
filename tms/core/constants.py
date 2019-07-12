# General
# ----------------------------------------------------------------------------
PRICE_MAX_DIGITS = 5
PRICE_DECIMAL_PLACES = 2

WEIGHT_MAX_DIGITS = 7
WEIGHT_DECIMAL_PLACES = 3


# Info app
# ----------------------------------------------------------------------------
# product type choices
PRODUCT_CATEGORY_GASOLINE = 'G'
PRODUCT_CATEGORY_OIL = 'O'
PRODUCT_CATEGORY = (
    (PRODUCT_CATEGORY_GASOLINE, '汽油'),
    (PRODUCT_CATEGORY_OIL, '油')
)

# station type
STATION_TYPE_LOADING_STATION = 'L'
STATION_TYPE_UNLOADING_STATION = 'U'
STATION_TYPE_QUALITY_STATION = 'Q'
STATION_TYPE_OIL_STATION = 'O'
STATION_TYPE_BLACK_DOT = 'B'
STATION_TYPE = (
    (STATION_TYPE_LOADING_STATION, '装货地'),
    (STATION_TYPE_UNLOADING_STATION, '卸货地'),
    (STATION_TYPE_QUALITY_STATION, '质检点'),
    (STATION_TYPE_OIL_STATION, '合作油站'),
    (STATION_TYPE_BLACK_DOT, '黑点'),
)

# duration unit choices
TIME_MEASURE_UNIT_MINITE = 'M'
TIME_MEASURE_UNIT_HOUR = 'H'
TIME_MEASURE_UNIT = (
    (TIME_MEASURE_UNIT_MINITE, '分钟'),
    (TIME_MEASURE_UNIT_HOUR, '小时'),
)

PRICE_VARY_DURATION_UNIT_WEEK = 'W'
PRICE_VARY_DURATION_UNIT_MONTH = 'M'
PRICE_VARY_DURATION_UNIT_YEAR = 'Y'
PRICE_VARY_DURATION_UNIT = (
    (PRICE_VARY_DURATION_UNIT_WEEK, '周'),
    (PRICE_VARY_DURATION_UNIT_MONTH, '月'),
    (PRICE_VARY_DURATION_UNIT_YEAR, '年')
)

# product unit measure choices
PRODUCT_WEIGHT_MEASURE_UNIT_LITRE = 'L'
PRODUCT_WEIGHT_MEASURE_UNIT_TON = 'T'
PRODUCT_WEIGHT_MEASURE_UNIT = (
    (PRODUCT_WEIGHT_MEASURE_UNIT_LITRE, '公升'),
    (PRODUCT_WEIGHT_MEASURE_UNIT_TON, '吨')
)


# Vehicle app - Vehicle constants
# ----------------------------------------------------------------------------
# vehicle model choices
VEHICLE_MODEL_TYPE_TRUCK = 'T'
VEHICLE_MODEL_TYPE_SEMI_TRAILER = 'S'
VEHICLE_MODEL_TYPE = (
    (VEHICLE_MODEL_TYPE_TRUCK, '牵引车'),
    (VEHICLE_MODEL_TYPE_SEMI_TRAILER, '半挂罐车')
)

# vehicle brand choices
VEHICLE_BRAND_TONGHUA = 'T'
VEHICLE_BRAND_LIBERATION = 'L'
VEHICLE_BRAND_YANGZHOU = 'Y'
VEHICLE_BRAND = (
    (VEHICLE_BRAND_TONGHUA, '通华'),
    (VEHICLE_BRAND_LIBERATION, '解放'),
    (VEHICLE_BRAND_YANGZHOU, '扬州中集')
)

# vehicle document type choices
VEHICLE_DOCUMENT_TYPE_D1 = '1'
VEHICLE_DOCUMENT_TYPE_D2 = '2'
VEHICLE_DOCUMENT_TYPE = (
    (VEHICLE_DOCUMENT_TYPE_D1, 'D1'),
    (VEHICLE_DOCUMENT_TYPE_D2, 'D2')
)

# vehicle status
VEHICLE_STATUS_AVAILABLE = 'A'
VEHICLE_STATUS_INWORK = 'P'
VEHICLE_STATUS_REPAIR = 'R'
VEHICLE_STATUS = (
    (VEHICLE_STATUS_AVAILABLE, 'Available'),
    (VEHICLE_STATUS_INWORK, 'In Work'),
    (VEHICLE_STATUS_REPAIR, 'Repair')
)

# vehicle maintenace type
VEHICLE_MAINTENANCE_REPAIR = 'R'
VEHICLE_MAINTENANCE = (
    (VEHICLE_MAINTENANCE_REPAIR, 'Repair'),
)

VEHICLE_USER_BIND_METHOD_BY_ADMIN = 'A'
VEHICLE_USER_BIND_METHOD_BY_JOB = 'J'
VEHICLE_USER_BIND_METHOD = (
    (VEHICLE_USER_BIND_METHOD_BY_ADMIN, 'By Admin'),
    (VEHICLE_USER_BIND_METHOD_BY_JOB, 'By Job')
)


# Account app - Account constants
# ----------------------------------------------------------------------------
# user role choices
USER_ROLE_ADMIN = 'A'
USER_ROLE_STAFF = 'S'
USER_ROLE_DRIVER = 'D'
USER_ROLE_ESCORT = 'E'
USER_ROLE_CUSTOMER = 'C'
USER_ROLE = (
    (USER_ROLE_ADMIN, '管理人员'),
    (USER_ROLE_STAFF, '工作人员'),
    (USER_ROLE_DRIVER, '驾驶人员'),
    (USER_ROLE_ESCORT, '押运人员'),
    (USER_ROLE_CUSTOMER, '客户')
)

# user document type choices
USER_DOCUMENT_TYPE_D1 = '1'
USER_DOCUMENT_TYPE_D2 = '2'
USER_DOCUMENT_TYPE = (
    (USER_DOCUMENT_TYPE_D1, 'D1'),
    (USER_DOCUMENT_TYPE_D2, 'D2')
)


# Order app - Order status constants
# ----------------------------------------------------------------------------
# order status choices
ORDER_STATUS_PENDING = 'P'
ORDER_STATUS_INPROGRESS = 'I'
ORDER_STATUS_COMPLETE = 'C'
ORDER_STATUS = (
    (ORDER_STATUS_PENDING, '未开始'),
    (ORDER_STATUS_INPROGRESS, '已开始'),
    (ORDER_STATUS_COMPLETE, '已完成')
)

# order source choices
ORDER_SOURCE_INTERNAL = 'I'
ORDER_SOURCE_CUSTOMER = 'C'
ORDER_SOURCE = (
    (ORDER_SOURCE_INTERNAL, '内部'),
    (ORDER_SOURCE_CUSTOMER, 'App')
)

# payment method choices
PAYMENT_METHOD_TON = 'T'
PAYMENT_METHOD_TON_PER_DISTANCE = 'D'
PAYMENT_METHOD_PRICE = 'P'
PAYMENT_METHOD = (
    (PAYMENT_METHOD_TON, '吨'),
    (PAYMENT_METHOD_TON_PER_DISTANCE, '吨/公里'),
    (PAYMENT_METHOD_PRICE, '一口价')
)


# job app
# ----------------------------------------------------------------------------
# job status choices
JOB_PROGRESS_COMPLETE = 0
JOB_PROGRESS_NOT_STARTED = 1
JOB_PROGRESS_TO_LOADING_STATION = 2
JOB_PROGRESS_ARRIVED_AT_LOADING_STATION = 3
JOB_PROGRESS_LOADING_AT_LOADING_STATION = 4
JOB_PROGRESS_FINISH_LOADING_AT_LOADING_STATION = 5
JOB_PROGRESS_TO_QUALITY_STATION = 6
JOB_PROGRESS_ARRIVED_AT_QUALITY_STATION = 7
JOB_PROGRESS_CHECKING_AT_QUALITY_STATION = 8
JOB_PROGRESS_FINISH_CHECKING_AT_QUALITY_STATION = 9
JOB_PROGRESS_TO_UNLOADING_STATION = 10
JOB_PRGORESS_ARRIVED_AT_UNLOADING_STATION = 11
JOB_PROGRESS_UNLOADING_AT_UNLOADING_STATION = 12
JOB_PROGRESS_FINISH_UNLOADING_AT_UNLOADING_STATION = 13

JOB_PROGRESS = (
    (
        JOB_PROGRESS_NOT_STARTED,
        'Job Progress - Not Started'
    ),
    (
        JOB_PROGRESS_COMPLETE,
        'Job Progress - Completed'
    ),
    (
        JOB_PROGRESS_TO_LOADING_STATION,
        'Job Progress - To Loading Station'
    ),
    (
        JOB_PROGRESS_ARRIVED_AT_LOADING_STATION,
        'Job Progress - Arrived at Loading Station'
    ),
    (
        JOB_PROGRESS_LOADING_AT_LOADING_STATION,
        'Job Progress - Loading at Loading Station'
    ),
    (
        JOB_PROGRESS_FINISH_LOADING_AT_LOADING_STATION,
        'Job Progress - Finish Loading at Loading Station'
    ),
    (
        JOB_PROGRESS_TO_QUALITY_STATION,
        'Job Progress - To Quality Station'
    ),
    (
        JOB_PROGRESS_ARRIVED_AT_QUALITY_STATION,
        'Job Progress - Arrived at Quality Station'
    ),
    (
        JOB_PROGRESS_CHECKING_AT_QUALITY_STATION,
        'Job Progress - Checking at Quality Station'
    ),
    (
        JOB_PROGRESS_FINISH_CHECKING_AT_QUALITY_STATION,
        'Job Progress - Finish Checking at Quality Station'
    ),
    (
        JOB_PROGRESS_TO_UNLOADING_STATION,
        'Job Progress - To Unloading Station'
    ),
    (
        JOB_PRGORESS_ARRIVED_AT_UNLOADING_STATION,
        'Job Progress - Arrived at Unloading Station'
    ),
    (
        JOB_PROGRESS_UNLOADING_AT_UNLOADING_STATION,
        'Job Progress - Unloading at Unloading Station'
    ),
    (
        JOB_PROGRESS_FINISH_UNLOADING_AT_UNLOADING_STATION,
        'Job Progress - Finish Unloading Station'
    )
)


# road app
# ----------------------------------------------------------------------------
ROUTE_PLANNING_POLICY_LEAST_TIME = 0
ROUTE_PLANNING_POLICY_LEAST_FEE = 1
ROUTE_PLANNING_POLICY_LEAST_DISTANCE = 2
ROUTE_PLANNING_POLICY = (
    (ROUTE_PLANNING_POLICY_LEAST_TIME, '最快捷模式'),
    (ROUTE_PLANNING_POLICY_LEAST_FEE, '最经济模式'),
    (ROUTE_PLANNING_POLICY_LEAST_DISTANCE, '最短距离模式')
)

# hr app
# ----------------------------------------------------------------------------
PERMISSION_TYPE_NO = 0
PERMISSION_TYPE_READ = 1
PERMISSION_TYPE_WRITE = 2
PERMISSION_TYPE = (
    (PERMISSION_TYPE_NO, 'No permission'),
    (PERMISSION_TYPE_READ, 'Read Permission'),
    (PERMISSION_TYPE_WRITE, 'Write Permission')
)

REST_REQUEST_ILL = 0
REST_REQUEST_PERSONAL = 1
REST_REQUEST_CATEGORY = (
    (REST_REQUEST_ILL, '病假'),
    (REST_REQUEST_PERSONAL, '私事'),
)


# notification app
# ----------------------------------------------------------------------------
# driver status
WORK_STATUS_AVAILABLE = 'A'
WORK_STATUS_DRIVING = 'D'
WORK_STATUS_NOT_AVAILABLE = 'N'
WORK_STATUS = (
    (WORK_STATUS_AVAILABLE, 'Available'),
    (WORK_STATUS_DRIVING, 'Driving'),
    (WORK_STATUS_NOT_AVAILABLE, 'Not Available')
)

# driver notification
DRIVER_NOTIFICATION_TYPE_JOB = 0
DRIVER_NOTIFICATION_TYPE_ENTER_AREA = 1
DRIVER_NOTIFICATION_TYPE_EXIT_AREA = 2
DRIVER_NOTIFICATION_TYPE_BLACK_DOT = 3

# staff notification
NOTIFICATION_REST_REQUEST = 10
NOTIFICATION_REST_REQUEST_APPROVED = 11
NOTIFICATION_REST_REQUEST_DECLINED = 12

NOTIFICATION_VEHICLE_REPAIR_REQUEST = 20
NOTIFICATION_VEHICLE_REPAIR_REQUEST_APPROVED = 21
NOTIFICATION_VEHICLE_REPAIR_REQUEST_DECLINED = 22

NOTIFICATION_PARKING_REQUEST = 30
NOTIFICATION_PARKING_REQUEST_APPROVED = 31
NOTIFICATION_PARKING_REQUEST_DECLINED = 32

NOTIFICATION_DRIVER_CHANGE_REQUEST = 40
NOTIFICATION_DRIVER_CHANGE_REQUEST_APPROVED = 41
NOTIFICATION_DRIVER_CHANGE_REQUEST_DECLINED = 42
NOTIFICATION_DRIVER_CHANGE_REQUEST_NEW_DRIVER = 43

NOTIFICATION_ESCORT_CHANGE_REQUEST = 50
NOTIFICATION_ESCORT_CHANGE_REQUEST_APPROVED = 51
NOTIFICATION_ESCORT_CHANGE_REQUEST_DECLINED = 52
NOTIFICATION_ESCORT_CHANGE_REQUEST_NEW_ESCORT = 53

NOTIFICATION_TRAFFIC_ACCIDENT = 60

NOTIFICATION_TYPE = (
    (DRIVER_NOTIFICATION_TYPE_JOB,
        'Job Notification'),
    (DRIVER_NOTIFICATION_TYPE_ENTER_AREA,
        'Enter Area Notification'),
    (DRIVER_NOTIFICATION_TYPE_EXIT_AREA,
        'Exit Area Notification'),
    (DRIVER_NOTIFICATION_TYPE_BLACK_DOT,
        'Black Dot Notification'),
    (NOTIFICATION_REST_REQUEST,
        'Rest Request Notification'),
    (NOTIFICATION_REST_REQUEST_APPROVED,
        'Rest Request Notification Approved'),
    (NOTIFICATION_REST_REQUEST_DECLINED,
        'Rest Request Notification Declined'),
    (NOTIFICATION_VEHICLE_REPAIR_REQUEST,
        'Vehicle Maintenance Notification'),
    (NOTIFICATION_VEHICLE_REPAIR_REQUEST_APPROVED,
        'Vehicle Maintenance Notification Approved'),
    (NOTIFICATION_VEHICLE_REPAIR_REQUEST_DECLINED,
        'Vehicle Maintenance Notification Declined'),
    (NOTIFICATION_PARKING_REQUEST,
        'Parking Request Notification'),
    (NOTIFICATION_PARKING_REQUEST_APPROVED,
        'Parking Request Notification Approved'),
    (NOTIFICATION_PARKING_REQUEST_DECLINED,
        'Parking Request Notification Declined'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST,
        'Driver Change Notification'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST_APPROVED,
        'Driver Change Notification Approved'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST_DECLINED,
        'Driver Change Notification Declined'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST_NEW_DRIVER,
        'Driver Change Notification New Driver'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST,
        'Escort Change Notification'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST_APPROVED,
        'Escort Change Notification Approved'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST_DECLINED,
        'Escort Change Notification Declined'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST_NEW_ESCORT,
        'Escort Change Notification New Escort'),
    (NOTIFICATION_TRAFFIC_ACCIDENT,
        'Traffic Accident Notification'),
)


# finance app
# ----------------------------------------------------------------------------
# bill document type
BILL_FROM_LOADING_STATION = 0
BILL_FROM_QUALITY_STATION = 1
BILL_FROM_UNLOADING_STATION = 2
BILL_FROM_OIL_STATION = 3
BILL_FROM_TRAFFIC = 4
BILL_FROM_OTHER = 5
BILL_CATEGORY = (
    (BILL_FROM_LOADING_STATION, 'Bill from Loading Station'),
    (BILL_FROM_QUALITY_STATION, 'Bill from Quality Station'),
    (BILL_FROM_UNLOADING_STATION, 'Bill from UnLoading Station'),
    (BILL_FROM_OIL_STATION, '加油'),
    (BILL_FROM_TRAFFIC, '路票'),
    (BILL_FROM_OTHER, '其他')
)

LOADING_STATION_BILL = 0
LOADING_STATION_BILL_SUB_CATEGORY = (
    (LOADING_STATION_BILL, 'Loading Station'),
)

QUALITY_STATION_BILL = 0
QUALITY_STATION_BILL_SUB_CATEGORY = (
    (QUALITY_STATION_BILL, 'Quality Station'),
)

UNLOADING_STATION_BILL = 0
UNLOADING_STATION_BILL_SUB_CATEGORY = (
    (UNLOADING_STATION_BILL, 'Unloading Station'),
)

OIL_BILL_BY_CARD = 0
OIL_BILL_BY_CASH = 1
OIL_BILL_BY_OTHER = 2
OIL_BILL_SUB_CATEGORY = (
    (OIL_BILL_BY_CARD, '油卡加油'),
    (OIL_BILL_BY_CASH, '现金加油'),
    (OIL_BILL_BY_OTHER, '小贾加油')
)

TRAFFIC_BILL_BY_CARD = 0
TRAFFIC_BILL_BY__WITHOUT_TICKET = 1
TRAFFIC_BILL_BY_CASH = 2
TRAFFIC_BILL_SUB_CATEGORY = (
    (TRAFFIC_BILL_BY_CARD, '鲁通卡刷卡'),
    (TRAFFIC_BILL_BY__WITHOUT_TICKET, '鲁通卡无票'),
    (TRAFFIC_BILL_BY_CASH, '路票现金')
)

PARKING_BILL = 0
WASH_BILL = 1
TOLL_FEE = 2
TRAFFIC_VIOLATION_BILL = 3
TRUCK_REPAIR_BILL = 4
MEAL_BILL = 5
STAY_BILL = 6
EXTRA_BILL = 7
OTHER_BILL_SUB_CATEGORY = (
    (PARKING_BILL, '停车场'),
    (WASH_BILL, '洗车费'),
    (TOLL_FEE, '带路费'),
    (TRAFFIC_VIOLATION_BILL, '违章费'),
    (TRUCK_REPAIR_BILL, '修车费'),
    (MEAL_BILL, '吃饭'),
    (STAY_BILL, '睡觉'),
    (EXTRA_BILL, '更多'),
)

TRAFFIC_VIOLATION_RED_LIGHT = 0
TRAFFIC_VIOLATION_TRUCK_LINE = 1
TRAFFIC_VIOLATION_OVER_SPEED = 2
TRAFFIC_VIOLATION_OVER_WEIGHT = 3
TRAFFIC_VIOLATION_DETAIL_CATEGORY = (
    (TRAFFIC_VIOLATION_RED_LIGHT, '闯红灯'),
    (TRAFFIC_VIOLATION_TRUCK_LINE, '不安导向车道行驶'),
    (TRAFFIC_VIOLATION_OVER_SPEED, '超速'),
    (TRAFFIC_VIOLATION_OVER_WEIGHT, '超重'),
)
