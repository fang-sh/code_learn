#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import pyspark
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row

# SparkContext.setSystemProperty('spark.driver.memory', '100g')
# SparkContext.setSystemProperty('spark.executor.memory', '10g')
# SparkContext.setSystemProperty('spark.executor.cores', '20')
# SparkContext.setSystemProperty('spark.sql.broadcastTimeout', '3000')
# SparkContext.setSystemProperty('spark.num.executors', '10')
# SparkContext.setSystemProperty('spark.ui.port', '8888')
# SparkContext.setSystemProperty('spark.driver.extraJavaOptions', '-XX:+UseG1GC')
# SparkContext.setSystemProperty('spark.executor.extraJavaOptions',  '-XX:+UseG1GC')
# SparkContext.setSystemProperty('spark.sql.autoBroadcastJoinThreshold', '-1')
# SparkContext.setCheckpointDir("path to directory")

# sc_conf = SparkConf()
# sc_conf.set('spark.driver.memory', '100G')
# sc_conf.set('spark.ui.port', '8888')
# sc_conf.set('spark.debug.maxToStringFields', '2000')
# sc_conf.set('spark.sql.windowExec.buffer.spill.threshold', '4096000')


sc = SparkContext()
spark = SparkSession(sc)


# rdd处理函数
def rdd_fun_list(x_list):
    for x in x_list:
        # 金额
        amt_list = [
            ['amt_1800', x.amt_1800],  # 30min
            ['balance_amt_1800', x.balance_amt_1800],

            ['amt_3600', x.amt_3600],  # 1h
            ['balance_amt_3600', x.balance_amt_3600],

            ['amt_86400', x.amt_86400],  # 1天
            ['balance_amt_86400', x.balance_amt_86400],

            ['amt_604800', x.amt_604800],  # 7天
            ['balance_amt_604800', x.balance_amt_604800],

            ['amt_1209600', x.amt_1209600],  # 14天
            ['balance_amt_1209600', x.balance_amt_1209600],

            ['amt_2592000', x.amt_2592000],  # 30天
            ['balance_amt_2592000', x.balance_amt_2592000],

        ]
        # 时间
        time_list = [
            ['u_time_1800', x.u_time_1800],
            ['u_time_3600', x.u_time_3600],
            ['u_time_86400', x.u_time_86400],
            ['u_time_604800', x.u_time_604800],
            ['u_time_1209600', x.u_time_1209600],
            ['u_time_2592000', x.u_time_2592000],

        ]
        res_dict = {}
        a_dict = {}

        # 1. money
        for col in amt_list:
            col_name = col[0]  # 列名

            # 如果col[1]为空时执行
            if not col[1]:
                # a_dict[col_name] = []
                a_dict[col_name + '_sum'] = float(np.nan)
                a_dict[col_name + '_avg'] = float(np.nan)
                a_dict[col_name + '_std'] = float(np.nan)
                a_dict[col_name + '_max'] = float(np.nan)
                a_dict[col_name + '_min'] = float(np.nan)
                a_dict[col_name + '_q1'] = float(np.nan)
                a_dict[col_name + '_q3'] = float(np.nan)
                a_dict[col_name + '_softNoise'] = float(np.nan)
                a_dict[col_name + '_hardNoise'] = float(np.nan)

                continue

            # col[1]非空时执行
            sort_list = []
            for item in col[1]:
                each = item.split('*')
                trx_amt = each[0]
                u_trx_time = each[1]

                sort_list.append([trx_amt, u_trx_time])

                # 按照时间戳timestemp排序
            sort_list = sorted(sort_list, key=lambda x: int(x[1]))
            tmp_list = []  # 临时list
            for ele in sort_list:
                tmp_list.append(float(ele[0]))

            # a_dict[col_name] = tmp_list
            a_dict[col_name + '_sum'] = float(np.sum(tmp_list))
            a_dict[col_name + '_avg'] = float(np.mean(tmp_list))
            a_dict[col_name + '_std'] = float(np.std(tmp_list))
            a_dict[col_name + '_max'] = float(np.max(tmp_list))
            a_dict[col_name + '_min'] = float(np.min(tmp_list))
            a_dict[col_name + '_q1'] = float(np.percentile(tmp_list,25)) # float(np.sort(tmp_list)[int(0.25 * len(tmp_list))])
            a_dict[col_name + '_q3'] = float(np.percentile(tmp_list,75)) # float(np.sort(tmp_list)[int(0.75 * len(tmp_list))])
            a_dict[col_name + '_softNoise'] = float(2.5 * a_dict[col_name + '_q3'] - 1.5 * a_dict[col_name + '_q1'])
            a_dict[col_name + '_hardNoise'] = float(4 * a_dict[col_name + '_q3'] - 3 * a_dict[col_name + '_q1'])

        # 2. timestamp
        for col in time_list:
            col_name = col[0]  # 列名

            # 如果col[1]为空时执行
            if not col[1]:
                # a_dict[col_name] = []
                a_dict[col_name + '_sum'] = float(np.nan)
                a_dict[col_name + '_avg'] = float(np.nan)
                a_dict[col_name + '_std'] = float(np.nan)
                a_dict[col_name + '_max'] = float(np.nan)
                a_dict[col_name + '_min'] = float(np.nan)
                a_dict[col_name + '_q1'] = float(np.nan)
                a_dict[col_name + '_q3'] = float(np.nan)
                a_dict[col_name + '_softNoise'] = float(np.nan)
                a_dict[col_name + '_hardNoise'] = float(np.nan)

                continue

            # col[1]非空时执行
            sort_list = []
            for timestamp in col[1]:
                each = int(timestamp)
                sort_list.append(each)
            sort_list = sorted(sort_list)

            # a_dict[col_name] = sort_list
            a_dict[col_name + '_sum'] = float(np.sum(sort_list))
            a_dict[col_name + '_avg'] = float(np.mean(sort_list))
            a_dict[col_name + '_std'] = float(np.std(sort_list))
            a_dict[col_name + '_max'] = float(np.max(sort_list))
            a_dict[col_name + '_min'] = float(np.min(sort_list))
            a_dict[col_name + '_q1'] = float(np.percentile(sort_list,25)) # float(np.sort(sort_list)[int(0.25 * len(sort_list))])
            a_dict[col_name + '_q3'] = float(np.percentile(sort_list,75)) # float(np.sort(sort_list)[int(0.75 * len(sort_list))])
            a_dict[col_name + '_softNoise'] = float(2.5 * a_dict[col_name + '_q3'] - 1.5 * a_dict[col_name + '_q1'])
            a_dict[col_name + '_hardNoise'] = float(4 * a_dict[col_name + '_q3'] - 3 * a_dict[col_name + '_q1'])

        b_dict = {
            'trx_id': x.trx_id,
            'cust_id': x.cust_id,
            'target_cust_id': x.target_cust_id,
            'flag_crdr': x.flag_crdr,
            'trx_amt': x.trx_amt,
            'balance_amt': x.balance_amt,
            'trx_date': x.trx_date,
            'trx_time': x.trx_time,
            'u_trx_time': x.u_trx_time,
            'cnt_1800': x.cnt_1800,
            'cnt_3600': x.cnt_3600,
            'cnt_86400': x.cnt_86400,
            'cnt_604800': x.cnt_604800,
            'cnt_1209600': x.cnt_1209600,
            'cnt_2592000': x.cnt_2592000,
            'crdr_0_1800': x.crdr_0_1800,
            'crdr_1_1800': x.crdr_1_1800,
            'crdr_0_3600': x.crdr_0_3600,
            'crdr_1_3600': x.crdr_1_3600,
            'crdr_0_86400': x.crdr_0_86400,
            'crdr_1_86400': x.crdr_1_86400,
            'crdr_0_604800': x.crdr_0_604800,
            'crdr_1_604800': x.crdr_1_604800,
            'crdr_0_1209600': x.crdr_0_1209600,
            'crdr_1_1209600': x.crdr_1_1209600,
            'crdr_0_2592000': x.crdr_0_2592000,
            'crdr_1_2592000': x.crdr_1_2592000,
        }

        # 合并a_dict和b_dict
        res_dict = {**b_dict, **a_dict}

        keys = list(res_dict.keys())

        yield [res_dict[k] for k in keys]

        # print(len(res_dict)) #223
        # print(list(res_dict.keys())) #获取列名
        # print('*******')
        # print(res_dict)

    # return res_dict


# --------------------------------------------------------------------------
# 从hdfs上下载文件
path = '/benchmark_data/fanxiqian/basic_data/fanxiqian_real_OriginData/'
ori_str = spark.read.parquet(path + 'ori_str')  # 可疑案宗表
ori_trx_new = spark.read.parquet(path + 'ori_trx_new')  # 交易详情表

# ori_retail_new = spark.read.parquet(path + 'ori_retail_new') #对私客户表
# ori_coporate = spark.read.parquet(path + 'ori_coporate') #对公客户表
# ori_account = spark.read.parquet(path + 'ori_account') #账户(卡)表


# --------------------------------------------------------------------------
# sql  所有交易详情数据，包含确定label的交易
ori_trx_new.registerTempTable('ori_trx_new')  # 注册临时表
# spark.sql("SET spark.sql.windowExec.buffer.spill.threshold = 4096000")

ori_trx_new_full = spark.sql(
    """
        select
                trx_id,
                cust_id,
                target_cust_id,
                flag_crdr,
                trx_amt,
                balance_amt,
                trx_date,
                trx_time,
                u_trx_time,
    
            -- 30min
            count(*) over(w_1800) as cnt_1800,
            collect_list(concat_ws('*',trx_amt,u_trx_time)) over(w_1800) as amt_1800,
            collect_list(concat_ws('*',balance_amt,u_trx_time)) over(w_1800) as balance_amt_1800,
            collect_list(concat_ws('*', u_trx_time)) over(w_1800) as u_time_1800,
    
            sum(if(flag_crdr=0,1,0)) over(w_1800) as crdr_0_1800,
            sum(if(flag_crdr=1,1,0)) over(w_1800) as crdr_1_1800,
    
            -- 1h
            count(*) over(w_3600) as cnt_3600,
            collect_list(concat_ws('*',trx_amt,u_trx_time)) over(w_3600) as amt_3600,
            collect_list(concat_ws('*',balance_amt,u_trx_time)) over(w_3600) as balance_amt_3600,
            collect_list(concat_ws('*', u_trx_time)) over(w_3600) as u_time_3600,
    
            sum(if(flag_crdr=0,1,0)) over(w_3600) as crdr_0_3600,
            sum(if(flag_crdr=1,1,0)) over(w_3600) as crdr_1_3600,
    
             -- 1天
            count(*) over(w_86400) as cnt_86400,
            collect_list(concat_ws('*',trx_amt,u_trx_time)) over(w_86400) as amt_86400,
            collect_list(concat_ws('*',balance_amt,u_trx_time)) over(w_86400) as balance_amt_86400,
            collect_list(concat_ws('*', u_trx_time)) over(w_86400) as u_time_86400,
    
            sum(if(flag_crdr=0,1,0)) over(w_86400) as crdr_0_86400,
            sum(if(flag_crdr=1,1,0)) over(w_86400) as crdr_1_86400,
    
             -- 7天
            count(*) over(w_604800) as cnt_604800,
            collect_list(concat_ws('*',trx_amt,u_trx_time)) over(w_604800) as amt_604800,
            collect_list(concat_ws('*',balance_amt,u_trx_time)) over(w_604800) as balance_amt_604800,
            collect_list(concat_ws('*', u_trx_time)) over(w_604800) as u_time_604800,
    
            sum(if(flag_crdr=0,1,0)) over(w_604800) as crdr_0_604800,
            sum(if(flag_crdr=1,1,0)) over(w_604800) as crdr_1_604800,
    
             -- 14天
            count(*) over(w_1209600) as cnt_1209600,
            collect_list(concat_ws('*',trx_amt,u_trx_time)) over(w_1209600) as amt_1209600,
            collect_list(concat_ws('*',balance_amt,u_trx_time)) over(w_1209600) as balance_amt_1209600,
            collect_list(concat_ws('*', u_trx_time)) over(w_1209600) as u_time_1209600,
    
            sum(if(flag_crdr=0,1,0)) over(w_1209600) as crdr_0_1209600,
            sum(if(flag_crdr=1,1,0)) over(w_1209600) as crdr_1_1209600,
    
             -- 30天
            count(*) over(w_2592000) as cnt_2592000,
            collect_list(concat_ws('*',trx_amt,u_trx_time)) over(w_2592000) as amt_2592000,
            collect_list(concat_ws('*',balance_amt,u_trx_time)) over(w_2592000) as balance_amt_2592000,
            collect_list(concat_ws('*', u_trx_time)) over(w_2592000) as u_time_2592000,
    
            sum(if(flag_crdr=0,1,0)) over(w_2592000) as crdr_0_2592000,
            sum(if(flag_crdr=1,1,0)) over(w_2592000) as crdr_1_2592000
    
        from(
                select
                    trx_id,
                    cust_id,
                    target_cust_id,
                    flag_crdr,
                    trx_amt,
                    balance_amt,
                    trx_date,
                    trx_time,
                    unix_timestamp(concat(trx_date, ' ', trx_time )) as u_trx_time
                from ori_trx_new
    
        )
        window
            -- w_300 as (partition by cust_id order by u_trx_time range between 300 preceding and 300 following), --5min
            w_1800 as (partition by cust_id order by u_trx_time range between 1800 preceding and 1800 following), --30min
            w_3600 as (partition by cust_id order by u_trx_time range between 3600 preceding and 3600 following), --1h
            -- w_7200 as (partition by cust_id order by u_trx_time range between 7200 preceding and 7200 following),--2h
            -- w_28800 as (partition by cust_id order by u_trx_time range between 28800 preceding and 28800 following),--8h
            w_86400 as (partition by cust_id order by u_trx_time range between 86400 preceding and 86400 following),--1天
            w_604800 as (partition by cust_id order by u_trx_time range between 604800 preceding and 604800 following),--7天
            w_1209600 as (partition by cust_id order by u_trx_time range between 1209600 preceding and 1209600 following),--14天
            w_2592000 as (partition by cust_id order by u_trx_time range between 2592000 preceding and 2592000 following)--30天
    
    """

)

# --------------------------------------------------------------------------
# 对应列名
col_list = ['trx_id',
            'cust_id',
            'target_cust_id',
            'flag_crdr',
            'trx_amt',
            'balance_amt',
            'trx_date',
            'trx_time',
            'u_trx_time',
            'cnt_1800',
            'cnt_3600',
            'cnt_86400',
            'cnt_604800',
            'cnt_1209600',
            'cnt_2592000',
            'crdr_0_1800',
            'crdr_1_1800',
            'crdr_0_3600',
            'crdr_1_3600',
            'crdr_0_86400',
            'crdr_1_86400',
            'crdr_0_604800',
            'crdr_1_604800',
            'crdr_0_1209600',
            'crdr_1_1209600',
            'crdr_0_2592000',
            'crdr_1_2592000',
            'amt_1800_sum',
            'amt_1800_avg',
            'amt_1800_std',
            'amt_1800_max',
            'amt_1800_min',
            'amt_1800_q1',
            'amt_1800_q3',
            'amt_1800_softNoise',
            'amt_1800_hardNoise',
            'balance_amt_1800_sum',
            'balance_amt_1800_avg',
            'balance_amt_1800_std',
            'balance_amt_1800_max',
            'balance_amt_1800_min',
            'balance_amt_1800_q1',
            'balance_amt_1800_q3',
            'balance_amt_1800_softNoise',
            'balance_amt_1800_hardNoise',
            'amt_3600_sum',
            'amt_3600_avg',
            'amt_3600_std',
            'amt_3600_max',
            'amt_3600_min',
            'amt_3600_q1',
            'amt_3600_q3',
            'amt_3600_softNoise',
            'amt_3600_hardNoise',
            'balance_amt_3600_sum',
            'balance_amt_3600_avg',
            'balance_amt_3600_std',
            'balance_amt_3600_max',
            'balance_amt_3600_min',
            'balance_amt_3600_q1',
            'balance_amt_3600_q3',
            'balance_amt_3600_softNoise',
            'balance_amt_3600_hardNoise',
            'amt_86400_sum',
            'amt_86400_avg',
            'amt_86400_std',
            'amt_86400_max',
            'amt_86400_min',
            'amt_86400_q1',
            'amt_86400_q3',
            'amt_86400_softNoise',
            'amt_86400_hardNoise',
            'balance_amt_86400_sum',
            'balance_amt_86400_avg',
            'balance_amt_86400_std',
            'balance_amt_86400_max',
            'balance_amt_86400_min',
            'balance_amt_86400_q1',
            'balance_amt_86400_q3',
            'balance_amt_86400_softNoise',
            'balance_amt_86400_hardNoise',
            'amt_604800_sum',
            'amt_604800_avg',
            'amt_604800_std',
            'amt_604800_max',
            'amt_604800_min',
            'amt_604800_q1',
            'amt_604800_q3',
            'amt_604800_softNoise',
            'amt_604800_hardNoise',
            'balance_amt_604800_sum',
            'balance_amt_604800_avg',
            'balance_amt_604800_std',
            'balance_amt_604800_max',
            'balance_amt_604800_min',
            'balance_amt_604800_q1',
            'balance_amt_604800_q3',
            'balance_amt_604800_softNoise',
            'balance_amt_604800_hardNoise',
            'amt_1209600_sum',
            'amt_1209600_avg',
            'amt_1209600_std',
            'amt_1209600_max',
            'amt_1209600_min',
            'amt_1209600_q1',
            'amt_1209600_q3',
            'amt_1209600_softNoise',
            'amt_1209600_hardNoise',
            'balance_amt_1209600_sum',
            'balance_amt_1209600_avg',
            'balance_amt_1209600_std',
            'balance_amt_1209600_max',
            'balance_amt_1209600_min',
            'balance_amt_1209600_q1',
            'balance_amt_1209600_q3',
            'balance_amt_1209600_softNoise',
            'balance_amt_1209600_hardNoise',
            'amt_2592000_sum',
            'amt_2592000_avg',
            'amt_2592000_std',
            'amt_2592000_max',
            'amt_2592000_min',
            'amt_2592000_q1',
            'amt_2592000_q3',
            'amt_2592000_softNoise',
            'amt_2592000_hardNoise',
            'balance_amt_2592000_sum',
            'balance_amt_2592000_avg',
            'balance_amt_2592000_std',
            'balance_amt_2592000_max',
            'balance_amt_2592000_min',
            'balance_amt_2592000_q1',
            'balance_amt_2592000_q3',
            'balance_amt_2592000_softNoise',
            'balance_amt_2592000_hardNoise',
            'u_time_1800_sum',
            'u_time_1800_avg',
            'u_time_1800_std',
            'u_time_1800_max',
            'u_time_1800_min',
            'u_time_1800_q1',
            'u_time_1800_q3',
            'u_time_1800_softNoise',
            'u_time_1800_hardNoise',
            'u_time_3600_sum',
            'u_time_3600_avg',
            'u_time_3600_std',
            'u_time_3600_max',
            'u_time_3600_min',
            'u_time_3600_q1',
            'u_time_3600_q3',
            'u_time_3600_softNoise',
            'u_time_3600_hardNoise',
            'u_time_86400_sum',
            'u_time_86400_avg',
            'u_time_86400_std',
            'u_time_86400_max',
            'u_time_86400_min',
            'u_time_86400_q1',
            'u_time_86400_q3',
            'u_time_86400_softNoise',
            'u_time_86400_hardNoise',
            'u_time_604800_sum',
            'u_time_604800_avg',
            'u_time_604800_std',
            'u_time_604800_max',
            'u_time_604800_min',
            'u_time_604800_q1',
            'u_time_604800_q3',
            'u_time_604800_softNoise',
            'u_time_604800_hardNoise',
            'u_time_1209600_sum',
            'u_time_1209600_avg',
            'u_time_1209600_std',
            'u_time_1209600_max',
            'u_time_1209600_min',
            'u_time_1209600_q1',
            'u_time_1209600_q3',
            'u_time_1209600_softNoise',
            'u_time_1209600_hardNoise',
            'u_time_2592000_sum',
            'u_time_2592000_avg',
            'u_time_2592000_std',
            'u_time_2592000_max',
            'u_time_2592000_min',
            'u_time_2592000_q1',
            'u_time_2592000_q3',
            'u_time_2592000_softNoise',
            'u_time_2592000_hardNoise']

# --------------------------------------------------------------------------
rdd_full = ori_trx_new_full.rdd.mapPartitions(lambda x: rdd_fun_list(x))
user_act_full = spark.createDataFrame(rdd_full, col_list)

# --------------------------------------------------------------------------
# 从user_act_full中进一步group by cust_id，获取统计信息
user_act_full.registerTempTable("user_act_full")  # 注册临时表
user_act_full2 = spark.sql(

    """
    select
        cust_id,
        avg(cnt_1800) as cnt_1800_avg,
        max(cnt_1800) as cnt_1800_max,
        min(cnt_1800) as cnt_1800_min,
        avg(cnt_3600) as cnt_3600_avg,
        max(cnt_3600) as cnt_3600_max,
        min(cnt_3600) as cnt_3600_min,
        avg(cnt_86400) as cnt_86400_avg,
        max(cnt_86400) as cnt_86400_max,
        min(cnt_86400) as cnt_86400_min,
        avg(cnt_604800) as cnt_604800_avg,
        max(cnt_604800) as cnt_604800_max,
        min(cnt_604800) as cnt_604800_min,
        avg(cnt_1209600) as cnt_1209600_avg,
        max(cnt_1209600) as cnt_1209600_max,
        min(cnt_1209600) as cnt_1209600_min,
        avg(cnt_2592000) as cnt_2592000_avg,
        max(cnt_2592000) as cnt_2592000_max,
        min(cnt_2592000) as cnt_2592000_min,
        avg(crdr_0_1800) as crdr_0_1800_avg,
        max(crdr_0_1800) as crdr_0_1800_max,
        min(crdr_0_1800) as crdr_0_1800_min,
        avg(crdr_1_1800) as crdr_1_1800_avg,
        max(crdr_1_1800) as crdr_1_1800_max,
        min(crdr_1_1800) as crdr_1_1800_min,
        avg(crdr_0_3600) as crdr_0_3600_avg,
        max(crdr_0_3600) as crdr_0_3600_max,
        min(crdr_0_3600) as crdr_0_3600_min,
        avg(crdr_1_3600) as crdr_1_3600_avg,
        max(crdr_1_3600) as crdr_1_3600_max,
        min(crdr_1_3600) as crdr_1_3600_min,
        avg(crdr_0_86400) as crdr_0_86400_avg,
        max(crdr_0_86400) as crdr_0_86400_max,
        min(crdr_0_86400) as crdr_0_86400_min,
        avg(crdr_1_86400) as crdr_1_86400_avg,
        max(crdr_1_86400) as crdr_1_86400_max,
        min(crdr_1_86400) as crdr_1_86400_min,
        avg(crdr_0_604800) as crdr_0_604800_avg,
        max(crdr_0_604800) as crdr_0_604800_max,
        min(crdr_0_604800) as crdr_0_604800_min,
        avg(crdr_1_604800) as crdr_1_604800_avg,
        max(crdr_1_604800) as crdr_1_604800_max,
        min(crdr_1_604800) as crdr_1_604800_min,
        avg(crdr_0_1209600) as crdr_0_1209600_avg,
        max(crdr_0_1209600) as crdr_0_1209600_max,
        min(crdr_0_1209600) as crdr_0_1209600_min,
        avg(crdr_1_1209600) as crdr_1_1209600_avg,
        max(crdr_1_1209600) as crdr_1_1209600_max,
        min(crdr_1_1209600) as crdr_1_1209600_min,
        avg(crdr_0_2592000) as crdr_0_2592000_avg,
        max(crdr_0_2592000) as crdr_0_2592000_max,
        min(crdr_0_2592000) as crdr_0_2592000_min,
        avg(crdr_1_2592000) as crdr_1_2592000_avg,
        max(crdr_1_2592000) as crdr_1_2592000_max,
        min(crdr_1_2592000) as crdr_1_2592000_min,
        avg(amt_1800_sum) as amt_1800_sum_avg,
        max(amt_1800_sum) as amt_1800_sum_max,
        min(amt_1800_sum) as amt_1800_sum_min,
        avg(amt_1800_avg) as amt_1800_avg_avg,
        max(amt_1800_avg) as amt_1800_avg_max,
        min(amt_1800_avg) as amt_1800_avg_min,
        avg(amt_1800_std) as amt_1800_std_avg,
        max(amt_1800_std) as amt_1800_std_max,
        min(amt_1800_std) as amt_1800_std_min,
        avg(amt_1800_max) as amt_1800_max_avg,
        max(amt_1800_max) as amt_1800_max_max,
        min(amt_1800_max) as amt_1800_max_min,
        avg(amt_1800_min) as amt_1800_min_avg,
        max(amt_1800_min) as amt_1800_min_max,
        min(amt_1800_min) as amt_1800_min_min,
        avg(amt_1800_q1) as amt_1800_q1_avg,
        max(amt_1800_q1) as amt_1800_q1_max,
        min(amt_1800_q1) as amt_1800_q1_min,
        avg(amt_1800_q3) as amt_1800_q3_avg,
        max(amt_1800_q3) as amt_1800_q3_max,
        min(amt_1800_q3) as amt_1800_q3_min,
        avg(amt_1800_softNoise) as amt_1800_softNoise_avg,
        max(amt_1800_softNoise) as amt_1800_softNoise_max,
        min(amt_1800_softNoise) as amt_1800_softNoise_min,
        avg(amt_1800_hardNoise) as amt_1800_hardNoise_avg,
        max(amt_1800_hardNoise) as amt_1800_hardNoise_max,
        min(amt_1800_hardNoise) as amt_1800_hardNoise_min,
        avg(balance_amt_1800_sum) as balance_amt_1800_sum_avg,
        max(balance_amt_1800_sum) as balance_amt_1800_sum_max,
        min(balance_amt_1800_sum) as balance_amt_1800_sum_min,
        avg(balance_amt_1800_avg) as balance_amt_1800_avg_avg,
        max(balance_amt_1800_avg) as balance_amt_1800_avg_max,
        min(balance_amt_1800_avg) as balance_amt_1800_avg_min,
        avg(balance_amt_1800_std) as balance_amt_1800_std_avg,
        max(balance_amt_1800_std) as balance_amt_1800_std_max,
        min(balance_amt_1800_std) as balance_amt_1800_std_min,
        avg(balance_amt_1800_max) as balance_amt_1800_max_avg,
        max(balance_amt_1800_max) as balance_amt_1800_max_max,
        min(balance_amt_1800_max) as balance_amt_1800_max_min,
        avg(balance_amt_1800_min) as balance_amt_1800_min_avg,
        max(balance_amt_1800_min) as balance_amt_1800_min_max,
        min(balance_amt_1800_min) as balance_amt_1800_min_min,
        avg(balance_amt_1800_q1) as balance_amt_1800_q1_avg,
        max(balance_amt_1800_q1) as balance_amt_1800_q1_max,
        min(balance_amt_1800_q1) as balance_amt_1800_q1_min,
        avg(balance_amt_1800_q3) as balance_amt_1800_q3_avg,
        max(balance_amt_1800_q3) as balance_amt_1800_q3_max,
        min(balance_amt_1800_q3) as balance_amt_1800_q3_min,
        avg(balance_amt_1800_softNoise) as balance_amt_1800_softNoise_avg,
        max(balance_amt_1800_softNoise) as balance_amt_1800_softNoise_max,
        min(balance_amt_1800_softNoise) as balance_amt_1800_softNoise_min,
        avg(balance_amt_1800_hardNoise) as balance_amt_1800_hardNoise_avg,
        max(balance_amt_1800_hardNoise) as balance_amt_1800_hardNoise_max,
        min(balance_amt_1800_hardNoise) as balance_amt_1800_hardNoise_min,
        avg(amt_3600_sum) as amt_3600_sum_avg,
        max(amt_3600_sum) as amt_3600_sum_max,
        min(amt_3600_sum) as amt_3600_sum_min,
        avg(amt_3600_avg) as amt_3600_avg_avg,
        max(amt_3600_avg) as amt_3600_avg_max,
        min(amt_3600_avg) as amt_3600_avg_min,
        avg(amt_3600_std) as amt_3600_std_avg,
        max(amt_3600_std) as amt_3600_std_max,
        min(amt_3600_std) as amt_3600_std_min,
        avg(amt_3600_max) as amt_3600_max_avg,
        max(amt_3600_max) as amt_3600_max_max,
        min(amt_3600_max) as amt_3600_max_min,
        avg(amt_3600_min) as amt_3600_min_avg,
        max(amt_3600_min) as amt_3600_min_max,
        min(amt_3600_min) as amt_3600_min_min,
        avg(amt_3600_q1) as amt_3600_q1_avg,
        max(amt_3600_q1) as amt_3600_q1_max,
        min(amt_3600_q1) as amt_3600_q1_min,
        avg(amt_3600_q3) as amt_3600_q3_avg,
        max(amt_3600_q3) as amt_3600_q3_max,
        min(amt_3600_q3) as amt_3600_q3_min,
        avg(amt_3600_softNoise) as amt_3600_softNoise_avg,
        max(amt_3600_softNoise) as amt_3600_softNoise_max,
        min(amt_3600_softNoise) as amt_3600_softNoise_min,
        avg(amt_3600_hardNoise) as amt_3600_hardNoise_avg,
        max(amt_3600_hardNoise) as amt_3600_hardNoise_max,
        min(amt_3600_hardNoise) as amt_3600_hardNoise_min,
        avg(balance_amt_3600_sum) as balance_amt_3600_sum_avg,
        max(balance_amt_3600_sum) as balance_amt_3600_sum_max,
        min(balance_amt_3600_sum) as balance_amt_3600_sum_min,
        avg(balance_amt_3600_avg) as balance_amt_3600_avg_avg,
        max(balance_amt_3600_avg) as balance_amt_3600_avg_max,
        min(balance_amt_3600_avg) as balance_amt_3600_avg_min,
        avg(balance_amt_3600_std) as balance_amt_3600_std_avg,
        max(balance_amt_3600_std) as balance_amt_3600_std_max,
        min(balance_amt_3600_std) as balance_amt_3600_std_min,
        avg(balance_amt_3600_max) as balance_amt_3600_max_avg,
        max(balance_amt_3600_max) as balance_amt_3600_max_max,
        min(balance_amt_3600_max) as balance_amt_3600_max_min,
        avg(balance_amt_3600_min) as balance_amt_3600_min_avg,
        max(balance_amt_3600_min) as balance_amt_3600_min_max,
        min(balance_amt_3600_min) as balance_amt_3600_min_min,
        avg(balance_amt_3600_q1) as balance_amt_3600_q1_avg,
        max(balance_amt_3600_q1) as balance_amt_3600_q1_max,
        min(balance_amt_3600_q1) as balance_amt_3600_q1_min,
        avg(balance_amt_3600_q3) as balance_amt_3600_q3_avg,
        max(balance_amt_3600_q3) as balance_amt_3600_q3_max,
        min(balance_amt_3600_q3) as balance_amt_3600_q3_min,
        avg(balance_amt_3600_softNoise) as balance_amt_3600_softNoise_avg,
        max(balance_amt_3600_softNoise) as balance_amt_3600_softNoise_max,
        min(balance_amt_3600_softNoise) as balance_amt_3600_softNoise_min,
        avg(balance_amt_3600_hardNoise) as balance_amt_3600_hardNoise_avg,
        max(balance_amt_3600_hardNoise) as balance_amt_3600_hardNoise_max,
        min(balance_amt_3600_hardNoise) as balance_amt_3600_hardNoise_min,
        avg(amt_86400_sum) as amt_86400_sum_avg,
        max(amt_86400_sum) as amt_86400_sum_max,
        min(amt_86400_sum) as amt_86400_sum_min,
        avg(amt_86400_avg) as amt_86400_avg_avg,
        max(amt_86400_avg) as amt_86400_avg_max,
        min(amt_86400_avg) as amt_86400_avg_min,
        avg(amt_86400_std) as amt_86400_std_avg,
        max(amt_86400_std) as amt_86400_std_max,
        min(amt_86400_std) as amt_86400_std_min,
        avg(amt_86400_max) as amt_86400_max_avg,
        max(amt_86400_max) as amt_86400_max_max,
        min(amt_86400_max) as amt_86400_max_min,
        avg(amt_86400_min) as amt_86400_min_avg,
        max(amt_86400_min) as amt_86400_min_max,
        min(amt_86400_min) as amt_86400_min_min,
        avg(amt_86400_q1) as amt_86400_q1_avg,
        max(amt_86400_q1) as amt_86400_q1_max,
        min(amt_86400_q1) as amt_86400_q1_min,
        avg(amt_86400_q3) as amt_86400_q3_avg,
        max(amt_86400_q3) as amt_86400_q3_max,
        min(amt_86400_q3) as amt_86400_q3_min,
        avg(amt_86400_softNoise) as amt_86400_softNoise_avg,
        max(amt_86400_softNoise) as amt_86400_softNoise_max,
        min(amt_86400_softNoise) as amt_86400_softNoise_min,
        avg(amt_86400_hardNoise) as amt_86400_hardNoise_avg,
        max(amt_86400_hardNoise) as amt_86400_hardNoise_max,
        min(amt_86400_hardNoise) as amt_86400_hardNoise_min,
        avg(balance_amt_86400_sum) as balance_amt_86400_sum_avg,
        max(balance_amt_86400_sum) as balance_amt_86400_sum_max,
        min(balance_amt_86400_sum) as balance_amt_86400_sum_min,
        avg(balance_amt_86400_avg) as balance_amt_86400_avg_avg,
        max(balance_amt_86400_avg) as balance_amt_86400_avg_max,
        min(balance_amt_86400_avg) as balance_amt_86400_avg_min,
        avg(balance_amt_86400_std) as balance_amt_86400_std_avg,
        max(balance_amt_86400_std) as balance_amt_86400_std_max,
        min(balance_amt_86400_std) as balance_amt_86400_std_min,
        avg(balance_amt_86400_max) as balance_amt_86400_max_avg,
        max(balance_amt_86400_max) as balance_amt_86400_max_max,
        min(balance_amt_86400_max) as balance_amt_86400_max_min,
        avg(balance_amt_86400_min) as balance_amt_86400_min_avg,
        max(balance_amt_86400_min) as balance_amt_86400_min_max,
        min(balance_amt_86400_min) as balance_amt_86400_min_min,
        avg(balance_amt_86400_q1) as balance_amt_86400_q1_avg,
        max(balance_amt_86400_q1) as balance_amt_86400_q1_max,
        min(balance_amt_86400_q1) as balance_amt_86400_q1_min,
        avg(balance_amt_86400_q3) as balance_amt_86400_q3_avg,
        max(balance_amt_86400_q3) as balance_amt_86400_q3_max,
        min(balance_amt_86400_q3) as balance_amt_86400_q3_min,
        avg(balance_amt_86400_softNoise) as balance_amt_86400_softNoise_avg,
        max(balance_amt_86400_softNoise) as balance_amt_86400_softNoise_max,
        min(balance_amt_86400_softNoise) as balance_amt_86400_softNoise_min,
        avg(balance_amt_86400_hardNoise) as balance_amt_86400_hardNoise_avg,
        max(balance_amt_86400_hardNoise) as balance_amt_86400_hardNoise_max,
        min(balance_amt_86400_hardNoise) as balance_amt_86400_hardNoise_min,
        avg(amt_604800_sum) as amt_604800_sum_avg,
        max(amt_604800_sum) as amt_604800_sum_max,
        min(amt_604800_sum) as amt_604800_sum_min,
        avg(amt_604800_avg) as amt_604800_avg_avg,
        max(amt_604800_avg) as amt_604800_avg_max,
        min(amt_604800_avg) as amt_604800_avg_min,
        avg(amt_604800_std) as amt_604800_std_avg,
        max(amt_604800_std) as amt_604800_std_max,
        min(amt_604800_std) as amt_604800_std_min,
        avg(amt_604800_max) as amt_604800_max_avg,
        max(amt_604800_max) as amt_604800_max_max,
        min(amt_604800_max) as amt_604800_max_min,
        avg(amt_604800_min) as amt_604800_min_avg,
        max(amt_604800_min) as amt_604800_min_max,
        min(amt_604800_min) as amt_604800_min_min,
        avg(amt_604800_q1) as amt_604800_q1_avg,
        max(amt_604800_q1) as amt_604800_q1_max,
        min(amt_604800_q1) as amt_604800_q1_min,
        avg(amt_604800_q3) as amt_604800_q3_avg,
        max(amt_604800_q3) as amt_604800_q3_max,
        min(amt_604800_q3) as amt_604800_q3_min,
        avg(amt_604800_softNoise) as amt_604800_softNoise_avg,
        max(amt_604800_softNoise) as amt_604800_softNoise_max,
        min(amt_604800_softNoise) as amt_604800_softNoise_min,
        avg(amt_604800_hardNoise) as amt_604800_hardNoise_avg,
        max(amt_604800_hardNoise) as amt_604800_hardNoise_max,
        min(amt_604800_hardNoise) as amt_604800_hardNoise_min,
        avg(balance_amt_604800_sum) as balance_amt_604800_sum_avg,
        max(balance_amt_604800_sum) as balance_amt_604800_sum_max,
        min(balance_amt_604800_sum) as balance_amt_604800_sum_min,
        avg(balance_amt_604800_avg) as balance_amt_604800_avg_avg,
        max(balance_amt_604800_avg) as balance_amt_604800_avg_max,
        min(balance_amt_604800_avg) as balance_amt_604800_avg_min,
        avg(balance_amt_604800_std) as balance_amt_604800_std_avg,
        max(balance_amt_604800_std) as balance_amt_604800_std_max,
        min(balance_amt_604800_std) as balance_amt_604800_std_min,
        avg(balance_amt_604800_max) as balance_amt_604800_max_avg,
        max(balance_amt_604800_max) as balance_amt_604800_max_max,
        min(balance_amt_604800_max) as balance_amt_604800_max_min,
        avg(balance_amt_604800_min) as balance_amt_604800_min_avg,
        max(balance_amt_604800_min) as balance_amt_604800_min_max,
        min(balance_amt_604800_min) as balance_amt_604800_min_min,
        avg(balance_amt_604800_q1) as balance_amt_604800_q1_avg,
        max(balance_amt_604800_q1) as balance_amt_604800_q1_max,
        min(balance_amt_604800_q1) as balance_amt_604800_q1_min,
        avg(balance_amt_604800_q3) as balance_amt_604800_q3_avg,
        max(balance_amt_604800_q3) as balance_amt_604800_q3_max,
        min(balance_amt_604800_q3) as balance_amt_604800_q3_min,
        avg(balance_amt_604800_softNoise) as balance_amt_604800_softNoise_avg,
        max(balance_amt_604800_softNoise) as balance_amt_604800_softNoise_max,
        min(balance_amt_604800_softNoise) as balance_amt_604800_softNoise_min,
        avg(balance_amt_604800_hardNoise) as balance_amt_604800_hardNoise_avg,
        max(balance_amt_604800_hardNoise) as balance_amt_604800_hardNoise_max,
        min(balance_amt_604800_hardNoise) as balance_amt_604800_hardNoise_min,
        avg(amt_1209600_sum) as amt_1209600_sum_avg,
        max(amt_1209600_sum) as amt_1209600_sum_max,
        min(amt_1209600_sum) as amt_1209600_sum_min,
        avg(amt_1209600_avg) as amt_1209600_avg_avg,
        max(amt_1209600_avg) as amt_1209600_avg_max,
        min(amt_1209600_avg) as amt_1209600_avg_min,
        avg(amt_1209600_std) as amt_1209600_std_avg,
        max(amt_1209600_std) as amt_1209600_std_max,
        min(amt_1209600_std) as amt_1209600_std_min,
        avg(amt_1209600_max) as amt_1209600_max_avg,
        max(amt_1209600_max) as amt_1209600_max_max,
        min(amt_1209600_max) as amt_1209600_max_min,
        avg(amt_1209600_min) as amt_1209600_min_avg,
        max(amt_1209600_min) as amt_1209600_min_max,
        min(amt_1209600_min) as amt_1209600_min_min,
        avg(amt_1209600_q1) as amt_1209600_q1_avg,
        max(amt_1209600_q1) as amt_1209600_q1_max,
        min(amt_1209600_q1) as amt_1209600_q1_min,
        avg(amt_1209600_q3) as amt_1209600_q3_avg,
        max(amt_1209600_q3) as amt_1209600_q3_max,
        min(amt_1209600_q3) as amt_1209600_q3_min,
        avg(amt_1209600_softNoise) as amt_1209600_softNoise_avg,
        max(amt_1209600_softNoise) as amt_1209600_softNoise_max,
        min(amt_1209600_softNoise) as amt_1209600_softNoise_min,
        avg(amt_1209600_hardNoise) as amt_1209600_hardNoise_avg,
        max(amt_1209600_hardNoise) as amt_1209600_hardNoise_max,
        min(amt_1209600_hardNoise) as amt_1209600_hardNoise_min,
        avg(balance_amt_1209600_sum) as balance_amt_1209600_sum_avg,
        max(balance_amt_1209600_sum) as balance_amt_1209600_sum_max,
        min(balance_amt_1209600_sum) as balance_amt_1209600_sum_min,
        avg(balance_amt_1209600_avg) as balance_amt_1209600_avg_avg,
        max(balance_amt_1209600_avg) as balance_amt_1209600_avg_max,
        min(balance_amt_1209600_avg) as balance_amt_1209600_avg_min,
        avg(balance_amt_1209600_std) as balance_amt_1209600_std_avg,
        max(balance_amt_1209600_std) as balance_amt_1209600_std_max,
        min(balance_amt_1209600_std) as balance_amt_1209600_std_min,
        avg(balance_amt_1209600_max) as balance_amt_1209600_max_avg,
        max(balance_amt_1209600_max) as balance_amt_1209600_max_max,
        min(balance_amt_1209600_max) as balance_amt_1209600_max_min,
        avg(balance_amt_1209600_min) as balance_amt_1209600_min_avg,
        max(balance_amt_1209600_min) as balance_amt_1209600_min_max,
        min(balance_amt_1209600_min) as balance_amt_1209600_min_min,
        avg(balance_amt_1209600_q1) as balance_amt_1209600_q1_avg,
        max(balance_amt_1209600_q1) as balance_amt_1209600_q1_max,
        min(balance_amt_1209600_q1) as balance_amt_1209600_q1_min,
        avg(balance_amt_1209600_q3) as balance_amt_1209600_q3_avg,
        max(balance_amt_1209600_q3) as balance_amt_1209600_q3_max,
        min(balance_amt_1209600_q3) as balance_amt_1209600_q3_min,
        avg(balance_amt_1209600_softNoise) as balance_amt_1209600_softNoise_avg,
        max(balance_amt_1209600_softNoise) as balance_amt_1209600_softNoise_max,
        min(balance_amt_1209600_softNoise) as balance_amt_1209600_softNoise_min,
        avg(balance_amt_1209600_hardNoise) as balance_amt_1209600_hardNoise_avg,
        max(balance_amt_1209600_hardNoise) as balance_amt_1209600_hardNoise_max,
        min(balance_amt_1209600_hardNoise) as balance_amt_1209600_hardNoise_min,
        avg(amt_2592000_sum) as amt_2592000_sum_avg,
        max(amt_2592000_sum) as amt_2592000_sum_max,
        min(amt_2592000_sum) as amt_2592000_sum_min,
        avg(amt_2592000_avg) as amt_2592000_avg_avg,
        max(amt_2592000_avg) as amt_2592000_avg_max,
        min(amt_2592000_avg) as amt_2592000_avg_min,
        avg(amt_2592000_std) as amt_2592000_std_avg,
        max(amt_2592000_std) as amt_2592000_std_max,
        min(amt_2592000_std) as amt_2592000_std_min,
        avg(amt_2592000_max) as amt_2592000_max_avg,
        max(amt_2592000_max) as amt_2592000_max_max,
        min(amt_2592000_max) as amt_2592000_max_min,
        avg(amt_2592000_min) as amt_2592000_min_avg,
        max(amt_2592000_min) as amt_2592000_min_max,
        min(amt_2592000_min) as amt_2592000_min_min,
        avg(amt_2592000_q1) as amt_2592000_q1_avg,
        max(amt_2592000_q1) as amt_2592000_q1_max,
        min(amt_2592000_q1) as amt_2592000_q1_min,
        avg(amt_2592000_q3) as amt_2592000_q3_avg,
        max(amt_2592000_q3) as amt_2592000_q3_max,
        min(amt_2592000_q3) as amt_2592000_q3_min,
        avg(amt_2592000_softNoise) as amt_2592000_softNoise_avg,
        max(amt_2592000_softNoise) as amt_2592000_softNoise_max,
        min(amt_2592000_softNoise) as amt_2592000_softNoise_min,
        avg(amt_2592000_hardNoise) as amt_2592000_hardNoise_avg,
        max(amt_2592000_hardNoise) as amt_2592000_hardNoise_max,
        min(amt_2592000_hardNoise) as amt_2592000_hardNoise_min,
        avg(balance_amt_2592000_sum) as balance_amt_2592000_sum_avg,
        max(balance_amt_2592000_sum) as balance_amt_2592000_sum_max,
        min(balance_amt_2592000_sum) as balance_amt_2592000_sum_min,
        avg(balance_amt_2592000_avg) as balance_amt_2592000_avg_avg,
        max(balance_amt_2592000_avg) as balance_amt_2592000_avg_max,
        min(balance_amt_2592000_avg) as balance_amt_2592000_avg_min,
        avg(balance_amt_2592000_std) as balance_amt_2592000_std_avg,
        max(balance_amt_2592000_std) as balance_amt_2592000_std_max,
        min(balance_amt_2592000_std) as balance_amt_2592000_std_min,
        avg(balance_amt_2592000_max) as balance_amt_2592000_max_avg,
        max(balance_amt_2592000_max) as balance_amt_2592000_max_max,
        min(balance_amt_2592000_max) as balance_amt_2592000_max_min,
        avg(balance_amt_2592000_min) as balance_amt_2592000_min_avg,
        max(balance_amt_2592000_min) as balance_amt_2592000_min_max,
        min(balance_amt_2592000_min) as balance_amt_2592000_min_min,
        avg(balance_amt_2592000_q1) as balance_amt_2592000_q1_avg,
        max(balance_amt_2592000_q1) as balance_amt_2592000_q1_max,
        min(balance_amt_2592000_q1) as balance_amt_2592000_q1_min,
        avg(balance_amt_2592000_q3) as balance_amt_2592000_q3_avg,
        max(balance_amt_2592000_q3) as balance_amt_2592000_q3_max,
        min(balance_amt_2592000_q3) as balance_amt_2592000_q3_min,
        avg(balance_amt_2592000_softNoise) as balance_amt_2592000_softNoise_avg,
        max(balance_amt_2592000_softNoise) as balance_amt_2592000_softNoise_max,
        min(balance_amt_2592000_softNoise) as balance_amt_2592000_softNoise_min,
        avg(balance_amt_2592000_hardNoise) as balance_amt_2592000_hardNoise_avg,
        max(balance_amt_2592000_hardNoise) as balance_amt_2592000_hardNoise_max,
        min(balance_amt_2592000_hardNoise) as balance_amt_2592000_hardNoise_min,
        avg(u_time_1800_sum) as u_time_1800_sum_avg,
        max(u_time_1800_sum) as u_time_1800_sum_max,
        min(u_time_1800_sum) as u_time_1800_sum_min,
        avg(u_time_1800_avg) as u_time_1800_avg_avg,
        max(u_time_1800_avg) as u_time_1800_avg_max,
        min(u_time_1800_avg) as u_time_1800_avg_min,
        avg(u_time_1800_std) as u_time_1800_std_avg,
        max(u_time_1800_std) as u_time_1800_std_max,
        min(u_time_1800_std) as u_time_1800_std_min,
        avg(u_time_1800_max) as u_time_1800_max_avg,
        max(u_time_1800_max) as u_time_1800_max_max,
        min(u_time_1800_max) as u_time_1800_max_min,
        avg(u_time_1800_min) as u_time_1800_min_avg,
        max(u_time_1800_min) as u_time_1800_min_max,
        min(u_time_1800_min) as u_time_1800_min_min,
        avg(u_time_1800_q1) as u_time_1800_q1_avg,
        max(u_time_1800_q1) as u_time_1800_q1_max,
        min(u_time_1800_q1) as u_time_1800_q1_min,
        avg(u_time_1800_q3) as u_time_1800_q3_avg,
        max(u_time_1800_q3) as u_time_1800_q3_max,
        min(u_time_1800_q3) as u_time_1800_q3_min,
        avg(u_time_1800_softNoise) as u_time_1800_softNoise_avg,
        max(u_time_1800_softNoise) as u_time_1800_softNoise_max,
        min(u_time_1800_softNoise) as u_time_1800_softNoise_min,
        avg(u_time_1800_hardNoise) as u_time_1800_hardNoise_avg,
        max(u_time_1800_hardNoise) as u_time_1800_hardNoise_max,
        min(u_time_1800_hardNoise) as u_time_1800_hardNoise_min,
        avg(u_time_3600_sum) as u_time_3600_sum_avg,
        max(u_time_3600_sum) as u_time_3600_sum_max,
        min(u_time_3600_sum) as u_time_3600_sum_min,
        avg(u_time_3600_avg) as u_time_3600_avg_avg,
        max(u_time_3600_avg) as u_time_3600_avg_max,
        min(u_time_3600_avg) as u_time_3600_avg_min,
        avg(u_time_3600_std) as u_time_3600_std_avg,
        max(u_time_3600_std) as u_time_3600_std_max,
        min(u_time_3600_std) as u_time_3600_std_min,
        avg(u_time_3600_max) as u_time_3600_max_avg,
        max(u_time_3600_max) as u_time_3600_max_max,
        min(u_time_3600_max) as u_time_3600_max_min,
        avg(u_time_3600_min) as u_time_3600_min_avg,
        max(u_time_3600_min) as u_time_3600_min_max,
        min(u_time_3600_min) as u_time_3600_min_min,
        avg(u_time_3600_q1) as u_time_3600_q1_avg,
        max(u_time_3600_q1) as u_time_3600_q1_max,
        min(u_time_3600_q1) as u_time_3600_q1_min,
        avg(u_time_3600_q3) as u_time_3600_q3_avg,
        max(u_time_3600_q3) as u_time_3600_q3_max,
        min(u_time_3600_q3) as u_time_3600_q3_min,
        avg(u_time_3600_softNoise) as u_time_3600_softNoise_avg,
        max(u_time_3600_softNoise) as u_time_3600_softNoise_max,
        min(u_time_3600_softNoise) as u_time_3600_softNoise_min,
        avg(u_time_3600_hardNoise) as u_time_3600_hardNoise_avg,
        max(u_time_3600_hardNoise) as u_time_3600_hardNoise_max,
        min(u_time_3600_hardNoise) as u_time_3600_hardNoise_min,
        avg(u_time_86400_sum) as u_time_86400_sum_avg,
        max(u_time_86400_sum) as u_time_86400_sum_max,
        min(u_time_86400_sum) as u_time_86400_sum_min,
        avg(u_time_86400_avg) as u_time_86400_avg_avg,
        max(u_time_86400_avg) as u_time_86400_avg_max,
        min(u_time_86400_avg) as u_time_86400_avg_min,
        avg(u_time_86400_std) as u_time_86400_std_avg,
        max(u_time_86400_std) as u_time_86400_std_max,
        min(u_time_86400_std) as u_time_86400_std_min,
        avg(u_time_86400_max) as u_time_86400_max_avg,
        max(u_time_86400_max) as u_time_86400_max_max,
        min(u_time_86400_max) as u_time_86400_max_min,
        avg(u_time_86400_min) as u_time_86400_min_avg,
        max(u_time_86400_min) as u_time_86400_min_max,
        min(u_time_86400_min) as u_time_86400_min_min,
        avg(u_time_86400_q1) as u_time_86400_q1_avg,
        max(u_time_86400_q1) as u_time_86400_q1_max,
        min(u_time_86400_q1) as u_time_86400_q1_min,
        avg(u_time_86400_q3) as u_time_86400_q3_avg,
        max(u_time_86400_q3) as u_time_86400_q3_max,
        min(u_time_86400_q3) as u_time_86400_q3_min,
        avg(u_time_86400_softNoise) as u_time_86400_softNoise_avg,
        max(u_time_86400_softNoise) as u_time_86400_softNoise_max,
        min(u_time_86400_softNoise) as u_time_86400_softNoise_min,
        avg(u_time_86400_hardNoise) as u_time_86400_hardNoise_avg,
        max(u_time_86400_hardNoise) as u_time_86400_hardNoise_max,
        min(u_time_86400_hardNoise) as u_time_86400_hardNoise_min,
        avg(u_time_604800_sum) as u_time_604800_sum_avg,
        max(u_time_604800_sum) as u_time_604800_sum_max,
        min(u_time_604800_sum) as u_time_604800_sum_min,
        avg(u_time_604800_avg) as u_time_604800_avg_avg,
        max(u_time_604800_avg) as u_time_604800_avg_max,
        min(u_time_604800_avg) as u_time_604800_avg_min,
        avg(u_time_604800_std) as u_time_604800_std_avg,
        max(u_time_604800_std) as u_time_604800_std_max,
        min(u_time_604800_std) as u_time_604800_std_min,
        avg(u_time_604800_max) as u_time_604800_max_avg,
        max(u_time_604800_max) as u_time_604800_max_max,
        min(u_time_604800_max) as u_time_604800_max_min,
        avg(u_time_604800_min) as u_time_604800_min_avg,
        max(u_time_604800_min) as u_time_604800_min_max,
        min(u_time_604800_min) as u_time_604800_min_min,
        avg(u_time_604800_q1) as u_time_604800_q1_avg,
        max(u_time_604800_q1) as u_time_604800_q1_max,
        min(u_time_604800_q1) as u_time_604800_q1_min,
        avg(u_time_604800_q3) as u_time_604800_q3_avg,
        max(u_time_604800_q3) as u_time_604800_q3_max,
        min(u_time_604800_q3) as u_time_604800_q3_min,
        avg(u_time_604800_softNoise) as u_time_604800_softNoise_avg,
        max(u_time_604800_softNoise) as u_time_604800_softNoise_max,
        min(u_time_604800_softNoise) as u_time_604800_softNoise_min,
        avg(u_time_604800_hardNoise) as u_time_604800_hardNoise_avg,
        max(u_time_604800_hardNoise) as u_time_604800_hardNoise_max,
        min(u_time_604800_hardNoise) as u_time_604800_hardNoise_min,
        avg(u_time_1209600_sum) as u_time_1209600_sum_avg,
        max(u_time_1209600_sum) as u_time_1209600_sum_max,
        min(u_time_1209600_sum) as u_time_1209600_sum_min,
        avg(u_time_1209600_avg) as u_time_1209600_avg_avg,
        max(u_time_1209600_avg) as u_time_1209600_avg_max,
        min(u_time_1209600_avg) as u_time_1209600_avg_min,
        avg(u_time_1209600_std) as u_time_1209600_std_avg,
        max(u_time_1209600_std) as u_time_1209600_std_max,
        min(u_time_1209600_std) as u_time_1209600_std_min,
        avg(u_time_1209600_max) as u_time_1209600_max_avg,
        max(u_time_1209600_max) as u_time_1209600_max_max,
        min(u_time_1209600_max) as u_time_1209600_max_min,
        avg(u_time_1209600_min) as u_time_1209600_min_avg,
        max(u_time_1209600_min) as u_time_1209600_min_max,
        min(u_time_1209600_min) as u_time_1209600_min_min,
        avg(u_time_1209600_q1) as u_time_1209600_q1_avg,
        max(u_time_1209600_q1) as u_time_1209600_q1_max,
        min(u_time_1209600_q1) as u_time_1209600_q1_min,
        avg(u_time_1209600_q3) as u_time_1209600_q3_avg,
        max(u_time_1209600_q3) as u_time_1209600_q3_max,
        min(u_time_1209600_q3) as u_time_1209600_q3_min,
        avg(u_time_1209600_softNoise) as u_time_1209600_softNoise_avg,
        max(u_time_1209600_softNoise) as u_time_1209600_softNoise_max,
        min(u_time_1209600_softNoise) as u_time_1209600_softNoise_min,
        avg(u_time_1209600_hardNoise) as u_time_1209600_hardNoise_avg,
        max(u_time_1209600_hardNoise) as u_time_1209600_hardNoise_max,
        min(u_time_1209600_hardNoise) as u_time_1209600_hardNoise_min,
        avg(u_time_2592000_sum) as u_time_2592000_sum_avg,
        max(u_time_2592000_sum) as u_time_2592000_sum_max,
        min(u_time_2592000_sum) as u_time_2592000_sum_min,
        avg(u_time_2592000_avg) as u_time_2592000_avg_avg,
        max(u_time_2592000_avg) as u_time_2592000_avg_max,
        min(u_time_2592000_avg) as u_time_2592000_avg_min,
        avg(u_time_2592000_std) as u_time_2592000_std_avg,
        max(u_time_2592000_std) as u_time_2592000_std_max,
        min(u_time_2592000_std) as u_time_2592000_std_min,
        avg(u_time_2592000_max) as u_time_2592000_max_avg,
        max(u_time_2592000_max) as u_time_2592000_max_max,
        min(u_time_2592000_max) as u_time_2592000_max_min,
        avg(u_time_2592000_min) as u_time_2592000_min_avg,
        max(u_time_2592000_min) as u_time_2592000_min_max,
        min(u_time_2592000_min) as u_time_2592000_min_min,
        avg(u_time_2592000_q1) as u_time_2592000_q1_avg,
        max(u_time_2592000_q1) as u_time_2592000_q1_max,
        min(u_time_2592000_q1) as u_time_2592000_q1_min,
        avg(u_time_2592000_q3) as u_time_2592000_q3_avg,
        max(u_time_2592000_q3) as u_time_2592000_q3_max,
        min(u_time_2592000_q3) as u_time_2592000_q3_min,
        avg(u_time_2592000_softNoise) as u_time_2592000_softNoise_avg,
        max(u_time_2592000_softNoise) as u_time_2592000_softNoise_max,
        min(u_time_2592000_softNoise) as u_time_2592000_softNoise_min,
        avg(u_time_2592000_hardNoise) as u_time_2592000_hardNoise_avg,
        max(u_time_2592000_hardNoise) as u_time_2592000_hardNoise_max,
        min(u_time_2592000_hardNoise) as u_time_2592000_hardNoise_min



    from user_act_full
    group by cust_id
    """
)

# --------------------------------------------------------------------------
# 保存最终的df full
user_act_full2.write.mode('overwrite').parquet("hdfs:///benchmark_data/fanxiqian/basic_data/user_action/user_action_all")




