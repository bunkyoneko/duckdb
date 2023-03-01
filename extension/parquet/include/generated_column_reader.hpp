//===----------------------------------------------------------------------===//
//                         DuckDB
//
// generated_column_reader.hpp
//
//
//===----------------------------------------------------------------------===//

#pragma once

#ifndef DUCKDB_AMALGAMATION
#include "duckdb/common/limits.hpp"
#endif
#include "column_reader.hpp"
#include "templated_column_reader.hpp"

namespace duckdb {

//! Reads a constant that is not read from the parquet file but instead generated by the parquet reader, used for
//! filename column. Can be used for handling hive partitioning later.
class GeneratedConstantColumnReader : public ColumnReader {
public:
	GeneratedConstantColumnReader(ParquetReader &reader, LogicalType type_p, const SchemaElement &schema_p,
	                              idx_t schema_idx_p, idx_t max_define_p, idx_t max_repeat_p, Value constant);
	Value constant;

public:
	idx_t Read(uint64_t num_values, parquet_filter_t &filter, uint8_t *define_out, uint8_t *repeat_out,
	           Vector &result) override;

	unique_ptr<BaseStatistics> Stats(idx_t row_group_idx_p, const std::vector<ColumnChunk> &columns) override {
		switch (type.id()) {
		case LogicalTypeId::VARCHAR: {
			auto string_stats = make_unique<StringStatistics>(type);
			string string = constant.ToString();
			string_stats->Update(string);
			string_stats->max_string_length = string.length();
			return std::move(string_stats);
		}
		default:
			return nullptr;
		}
	};

	void InitializeRead(idx_t row_group_idx_p, const std::vector<ColumnChunk> &columns,
	                    TProtocol &protocol_p) override {
		return;
	};
	void Skip(idx_t num_values) override {
		return;
	}
	idx_t GroupRowsAvailable() override {
		return NumericLimits<idx_t>::Maximum();
	};
	uint64_t TotalCompressedSize() override {
		return 0;
	}
	idx_t FileOffset() const override {
		return 0;
	}
	void RegisterPrefetch(ThriftFileTransport &transport, bool allow_merge) override {
	}
};

} // namespace duckdb
