from flaskr.i18n import _

BUY_STATUS_INIT = 501
BUY_STATUS_SUCCESS = 502
BUY_STATUS_REFUND = 503
BUY_STATUS_TO_BE_PAID = 504
BUY_STATUS_TIMEOUT = 505

ATTEND_STATUS_NOT_STARTED = 601
ATTEND_STATUS_IN_PROGRESS = 602
ATTEND_STATUS_COMPLETED = 603
ATTEND_STATUS_REFUND = 604
ATTEND_STATUS_LOCKED = 605
ATTEND_STATUS_UNAVAILABE = 606
ATTEND_STATUS_BRANCH = 607
ATTEND_STATUS_RESET = 608
ATTEND_STATUS_NOT_EXIST = -1
BUY_STATUS_TYPES = {
    "初始化": BUY_STATUS_INIT,
    "购买成功": BUY_STATUS_SUCCESS,
    "退款": BUY_STATUS_REFUND,
    "待支付": BUY_STATUS_TO_BE_PAID,
    "已过期": BUY_STATUS_TIMEOUT,
}

BUY_STATUS_VALUES = {
    BUY_STATUS_INIT: "初始化",
    BUY_STATUS_SUCCESS: "购买成功",
    BUY_STATUS_REFUND: "退款",
    BUY_STATUS_TO_BE_PAID: "待支付",
    BUY_STATUS_TIMEOUT: "已过期",
}

ATTEND_STATUS_TYPES = {
    "可学习": ATTEND_STATUS_NOT_STARTED,
    "正在学": ATTEND_STATUS_IN_PROGRESS,
    "已完成": ATTEND_STATUS_COMPLETED,
    "退款": ATTEND_STATUS_REFUND,
    "未解锁": ATTEND_STATUS_LOCKED,
    "不可用": ATTEND_STATUS_UNAVAILABE,
    "分支": ATTEND_STATUS_BRANCH,
    "重置": ATTEND_STATUS_RESET,
}


def get_attend_status_values():
    return {
        ATTEND_STATUS_NOT_STARTED: _("ORDER.ATTEND_STATUS_NOT_STARTED"),
        ATTEND_STATUS_IN_PROGRESS: _("ORDER.ATTEND_STATUS_IN_PROGRESS"),
        ATTEND_STATUS_COMPLETED: _("ORDER.ATTEND_STATUS_COMPLETED"),
        ATTEND_STATUS_REFUND: _("ORDER.ATTEND_STATUS_REFUND"),
        ATTEND_STATUS_LOCKED: _("ORDER.ATTEND_STATUS_LOCKED"),
        ATTEND_STATUS_UNAVAILABE: _("ORDER.ATTEND_STATUS_UNAVAILABE"),
        ATTEND_STATUS_BRANCH: _("ORDER.ATTEND_STATUS_BRANCH"),
        ATTEND_STATUS_RESET: _("ORDER.ATTEND_STATUS_RESET"),
    }


DISCOUNT_TYPE_FIXED = 701
DISCOUNT_TYPE_PERCENT = 702

DISCOUNT_TYPE_TYPES = {"固定金额": DISCOUNT_TYPE_FIXED, "百分比": DISCOUNT_TYPE_PERCENT}

DISCOUNT_TYPE_VALUES = {
    DISCOUNT_TYPE_FIXED: "固定金额",
    DISCOUNT_TYPE_PERCENT: "百分比",
}


DISCOUNT_APPLY_TYPE_ALL = 801
DISCOUNT_APPLY_TYPE_SPECIFIC = 802

DISCOUNT_APPLY_TYPE_TYPES = {
    "通用折扣码": DISCOUNT_APPLY_TYPE_ALL,
    "一单一码": DISCOUNT_APPLY_TYPE_SPECIFIC,
}


DISCOUNT_APPLY_TYPE_VALUES = {
    DISCOUNT_APPLY_TYPE_ALL: "通用折扣码",
    DISCOUNT_APPLY_TYPE_SPECIFIC: "一单一码",
}


DISCOUNT_STATUS_INACTIVE = 901
DISCOUNT_STATUS_ACTIVE = 902
DISCOUNT_STATUS_USED = 903
DISCOUNT_STATUS_TIMEOUT = 904


DISCOUNT_STATUS_TYPES = {
    "未激活": DISCOUNT_STATUS_INACTIVE,
    "激活": DISCOUNT_STATUS_ACTIVE,
    "已使用": DISCOUNT_STATUS_USED,
    "已过期": DISCOUNT_STATUS_TIMEOUT,
}

DISCOUNT_STATUS_VALUES = {
    DISCOUNT_STATUS_INACTIVE: "未激活",
    DISCOUNT_STATUS_ACTIVE: "激活",
    DISCOUNT_STATUS_USED: "已使用",
    DISCOUNT_STATUS_TIMEOUT: "已过期",
}
